#!/usr/bin/env python
#
#    Copyright (c) 2007 Corey Goldberg (corey@goldb.org)
#    License: GNU GPLv3
#
#    This file is part of Pylot.
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.  See the GNU General Public License 
#    for more details.
#


import glob
import corestats
import graph
import reportwriter



def generate_results(dir):
    merged_log = merge_log_files(dir)
    epoch_timings = list_timings(merged_log)
    
    # throughput
    epochs = [int(x[0]) for x in epoch_timings] # grab just the epochs as rounded-down secs
    tps = calc_throughputs(epochs) # dict of secs and throughputs
    graph.tp_graph(tps, dir=dir + '/')
    
    # response times
    # subtract start times so we have resp times by elapsed time starting at zero
    start_epoch = epoch_timings[0][0]
    based_timings = [((epoch_timing[0] - start_epoch), epoch_timing[1]) for epoch_timing in epoch_timings] 
    graph.resp_graph(based_timings, dir=dir + '/')
    
    resp_data_set = [x[1] for x in epoch_timings] # grab just the timings
    stats = corestats.Stats(resp_data_set)
    
    # calc the stats and load up a dictionary with the results
    stat_dict = {}
    stat_dict['count'] = stats.count()
    stat_dict['avg'] = stats.avg()
    stat_dict['stdev'] = stats.stdev()
    stat_dict['min'] = stats.min()
    stat_dict['max'] = stats.max()
    stat_dict['50pct'] = stats.percentile(50)
    stat_dict['80pct'] = stats.percentile(80)
    stat_dict['90pct'] = stats.percentile(90)
    stat_dict['95pct'] = stats.percentile(95)
    stat_dict['99pct'] = stats.percentile(99)
    

    
    
    print 'count:', stats.count()
    print 'avg:', stats.avg()
    print 'stdev:', stats.stdev()
    print 'min:', stats.min()
    print 'max:', stats.max()
    print '50 pct:', stats.percentile(50)
    print '80 pct:', stats.percentile(80)
    print '90 pct:', stats.percentile(90)
    print '95 pct:', stats.percentile(95)
    print '99 pct:', stats.percentile(99)
    
    

    
    
    fh = open(dir + '/results.html', 'w')
    reportwriter.write_head_html(fh)
    reportwriter.write_starting_content(fh)
    reportwriter.write_images(fh)
    reportwriter.write_closing_html(fh)
    fh.close()
    

    
def merge_log_files(dir):
    merged_file = []    
    for filename in glob.glob(dir + r'/*.psv'):
        fh = open(filename, 'rb')
        merged_file += fh.readlines()
        fh.close()
    return merged_file


def list_timings(merged_log):
    # create a list of tuples with our timing data sorted by epoch
    epoch_timings = []
    for line in merged_log:
        splat = line.split('|')
        epoch = splat[2].strip()
        response_time = splat[6].strip()
        epoch_timings.append((float(epoch), float(response_time)))
    epoch_timings.sort()
    return epoch_timings
    
    
def calc_throughputs(epochs):
    # load up a dictionary with epochs as keys and counts as values   
    # need start and end times
    start_sec = epochs[0]
    end_sec = epochs[-1]
    throughputs = {}
    for epoch in range(start_sec, end_sec + 1):
        count = epochs.count(epoch)       
        throughputs[epoch - start_sec] = count
    return throughputs



    
    
    
    
    