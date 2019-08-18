# -*- coding: utf-8 -*

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc 

class Plotter:
	def __init__(self, errors):
		self.errors = errors
		self.settings = {}
		self.ax = []
		self.subplot_offset = 0
		self.ohlc_series = {}
		
	def create_subplot(self, subplot_index, subplots_number, subplot_height_share):
		if subplot_index == 0:
			self.ax.append(plt.subplot2grid((sum(subplot_height_share) , 1), (self.subplot_offset, 0), rowspan = subplot_height_share[subplot_index]))
		else:
			self.ax.append(plt.subplot2grid((sum(subplot_height_share) , 1), (self.subplot_offset, 0), rowspan = subplot_height_share[subplot_index], sharex = self.ax[0]))
		
		self.subplot_offset += subplot_height_share[subplot_index]
		
	def set_seria_format(self, column, settings):
		seria_format = {}
		
		#ignore_missed_data
		if settings['plot_params']['ignore_missed_data'].get(column) != None:
			seria_format['ignore_missed_data'] = settings['plot_params']['ignore_missed_data'][column]
		else:
			seria_format['ignore_missed_data'] = settings['plot_params']['ignore_missed_data']['default']
		
		#column_line_type
		if settings['plot_params']['column_line_type'].get(column) != None:
			seria_format['line_type'] = settings['plot_params']['column_line_type'][column]
		else:
			seria_format['line_type'] = settings['plot_params']['column_line_type']['default']
		
		#column_marker_type
		if settings['plot_params']['column_marker_type'].get(column) != None:
			seria_format['marker_type'] = settings['plot_params']['column_marker_type'][column]
		else:
			seria_format['marker_type'] = settings['plot_params']['column_marker_type']['default']
		
		#column_line_width
		if settings['plot_params']['column_line_width'].get(column) != None:
			seria_format['line_width'] = float(settings['plot_params']['column_line_width'][column])
		else:
			seria_format['line_width'] = float(settings['plot_params']['column_line_width']['default'])
		
		#column_marker_size
		if settings['plot_params']['column_marker_size'].get(column) != None:
			seria_format['marker_size'] = float(settings['plot_params']['column_marker_size'][column])
		else:
			seria_format['marker_size'] = float(settings['plot_params']['column_marker_size']['default'])
		
		#column_line_color
		if settings['plot_params']['column_line_color'].get(column) != None:
			seria_format['line_color'] = settings['plot_params']['column_line_color'][column]
		else:
			seria_format['line_color'] = settings['plot_params']['column_line_color']['default']
		
		#column_marker_color
		if settings['plot_params']['column_marker_color'].get(column) != None:
			seria_format['marker_color'] = settings['plot_params']['column_marker_color'][column]
		else:
			seria_format['marker_color'] = settings['plot_params']['column_marker_color']['default']
		
		#column_marker_color
		if settings['plot_params']['column_marker_color'].get(column) != None:
			seria_format['marker_color'] = settings['plot_params']['column_marker_color'][column]
		else:
			seria_format['marker_color'] = settings['plot_params']['column_marker_color']['default']
		
		#column_alpha
		if settings['plot_params']['column_alpha'].get(column) != None:
			seria_format['alpha'] = settings['plot_params']['column_alpha'][column]
		else:
			seria_format['alpha'] = settings['plot_params']['column_alpha']['default']
			
		return seria_format
	
	
	
	def bind_seria_to_subplot(self, seria, subplot_index, seria_format):
		if seria_format['line_type'] == 'ohlc_o':
			self.ohlc_series['o'] = seria
		elif seria_format['line_type'] == 'ohlc_h':
			self.ohlc_series['h'] = seria
		elif seria_format['line_type'] == 'ohlc_l':
			self.ohlc_series['l'] = seria
		elif seria_format['line_type'] == 'ohlc_c':
			self.ohlc_series['c'] = seria
			x_ticks = range(len(seria))
			ohlc = []
			for x_tick in x_ticks:
				ohlc.append((x_tick, self.ohlc_series['o'][x_tick], self.ohlc_series['h'][x_tick], self.ohlc_series['l'][x_tick], self.ohlc_series['c'][x_tick]))
			candlestick_ohlc(self.ax[subplot_index], ohlc, width = 1, colorup = 'green', colordown = 'red', alpha = 0.7)
		else:
			x_ticks = np.arange(0, len(seria), 1)
			seria = np.array(seria).astype(np.double)
			if seria_format['ignore_missed_data'] == '1':
				s_mask = np.isfinite(seria)
				self.ax[subplot_index].plot(x_ticks[s_mask], seria[s_mask],
					linestyle = '--',
					linewidth = 3,
					color = 'red',
					marker = 'o',
					markeredgewidth = 0,
					markeredgecolor = 'green',
					markersize = 10,
					markerfacecolor = 'green'
				)
				
			else:
				self.ax[subplot_index].plot(x_ticks, seria,
					'.-',
					# color = seria_format['line_color'],
					linewidth = seria_format['line_width'],
					markersize = seria_format['marker_size'],
					alpha = seria_format['alpha']
				)
		
	def create_label(self, value, format):
		if format == 'dd-mm':
			return value['dd'] + '-' + value['mm']
		elif format == 'dd.mm':
			return value['dd'] + '.' + value['mm']
		elif format == 'dd.mm.yy':
			return value['dd'] + '.' + value['mm'] + '.' + value['yy']
		elif format == 'hh:mm':
			return value['hh'] + ':' + value['mm']
	
	def shape_x_labels(self, data, x_ticks_data_columns, x_ticks, x_labels_format,  major_x_ticks, minor_x_ticks, major_x_labels, minor_x_labels):
		for cnt in range(len(x_ticks_data_columns)):
			column = x_ticks_data_columns[cnt]
			format = x_labels_format[cnt]
			tick_key = x_ticks[cnt]
			last_tick_key = ''
			for data_cnt in range(len(data[column])):
				value = data[column][data_cnt]
				label = self.create_label(value, format) 
				if last_tick_key != value[tick_key]:
					last_tick_key = value[tick_key]
					if cnt == 0:
						major_x_ticks.append(data_cnt)
						major_x_labels.append('\n' +  label)
					else:
						minor_x_ticks.append(data_cnt)
						minor_x_labels.append(label)
	
	def set_x_labels(self, subplots_number, data, x_ticks_data_columns, x_ticks, x_labels_format):
		minor_x_ticks = []
		major_x_ticks = []
		minor_x_labels = []
		major_x_labels = []
		self.shape_x_labels(data, x_ticks_data_columns, x_ticks, x_labels_format, major_x_ticks, minor_x_ticks, major_x_labels, minor_x_labels)
		
		self.ax[0].set_xticks(minor_x_ticks, minor = True)
		self.ax[0].set_xticks(major_x_ticks)
		self.ax[0].set_xticklabels(major_x_labels)
		self.ax[0].set_xticklabels(minor_x_labels, minor = True)
		
		for subplot_index in range(subplots_number):
			plt.setp(self.ax[subplot_index].get_xticklabels(), visible = False)
			plt.setp(self.ax[subplot_index].get_xticklabels(minor = True), visible = False)
			self.ax[subplot_index].grid(which = 'minor', alpha = 0.4)
			self.ax[subplot_index].grid(which = 'major', alpha = 1)
			
		plt.setp(self.ax[subplots_number - 1].get_xticklabels(), visible = True)
		plt.setp(self.ax[subplots_number - 1].get_xticklabels(minor = True), visible = True)
		
	def plot_series(self, data_set, columns, settings):
		output_fig_folder = settings['output_fig_folder']
		output_fig_prefix_name = settings['output_fig_prefix_name']
		output_fig_ext = settings['output_fig_ext']
		plot_params = settings['plot_params']
		 # = settings['']
		
		
		subplot_height_share = settings['plot_params']['subplot_height_share'].split(',')
		for i in range(len(subplot_height_share)):
			subplot_height_share[i] = int(subplot_height_share[i])
		subplots_number = len(subplot_height_share)
		
		series = columns
		x_ticks_columns = settings['plot_params']['x_ticks_columns'].split(',')
		for i in range(len(x_ticks_columns)):
			series.remove(x_ticks_columns[i])
			
		# seria_to_subbplot_binding = settings['plotter']['seria_to_subbplot_binding']
		# x_ticks_data_columns = settings['plotter']['x_ticks_data_columns']
		#
		# x_labels_format = settings['plotter']['x_labels_format']
		
		plt.figure(figsize = (16, 9))
		for subplot_index in range(subplots_number):
			self.create_subplot(subplot_index, subplots_number, subplot_height_share)
		
		for column in series:
			col_idx = data_set['col_idx'][column]
			subplot_index = int(settings['plot_params']['subplot_column_binding'][column]) - 1
			seria_format = self.set_seria_format(column, settings)
			self.bind_seria_to_subplot(data_set[col_idx], subplot_index, seria_format)
			# break
			
		# self.set_x_labels(subplots_number, data, x_ticks_data_columns, x_ticks, x_labels_format)
			
		plt.tight_layout()
		plt.savefig(output_fig_folder + output_fig_prefix_name + output_fig_ext, dpi = 100)
		# plt.show()
		plt.close()
		
		
		
		