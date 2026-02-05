#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Извлечение AIS пакета из IQ сигнала
# Author: xxx
# Description: Чтение бинарного IQ файла с заданной частотой дискритезации
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import blocks, gr
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class read_bin_iq(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Извлечение AIS пакета из IQ сигнала", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Извлечение AIS пакета из IQ сигнала")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "read_bin_iq")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 192000
        self.ais_bitrate = ais_bitrate = 9600
        self.resampling_koeff = resampling_koeff = samp_rate/(4*ais_bitrate)
        self.ais_modulation_index = ais_modulation_index = 0.5
        self.transition_bw = transition_bw = 2000
        self.samp_rate_resample = samp_rate_resample = samp_rate/resampling_koeff
        self.pi = pi = 3.14159
        self.freq_low_ais = freq_low_ais = 161975000
        self.freq_high_ais_0 = freq_high_ais_0 = 162025000
        self.freq_center = freq_center = 162000000
        self.filter_span = filter_span = 9
        self.bandwidth_ais = bandwidth_ais = 25000
        self.ais_fsk_deviation_hz = ais_fsk_deviation_hz = ais_modulation_index * ais_bitrate / 2

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(resampling_koeff),
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
            8192, #size
            window.WIN_HAMMING, #wintype
            freq_low_ais, #fc
            samp_rate_resample, #bw
            'FIR', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.001)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            8192, #size
            window.WIN_HAMMING, #wintype
            freq_center, #fc
            samp_rate, #bw
            'Raw file source', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_2_0_1_0 = qtgui.time_sink_f(
            10000, #size
            samp_rate, #samp_rate
            'Demod', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2_0_1_0.set_update_time(0.010)
        self.qtgui_time_sink_x_2_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_2_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.025, 0, 0, '')
        self.qtgui_time_sink_x_2_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_2_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_2_0_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_1_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate_resample,
                (0.6*ais_bitrate),
                (0.5*ais_fsk_deviation_hz),
                window.WIN_HAMMING,
                1.0))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.low_pass(1, samp_rate, bandwidth_ais/2, transition_bw), (-23000), samp_rate)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff((samp_rate_resample / ais_bitrate), 0.0005, firdes.gaussian(gain=1.0, spb=samp_rate_resample / ais_bitrate,bt=0.4, ntaps=int(filter_span*samp_rate_resample / ais_bitrate)), 32, 0.5, 1.5, 1)
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(20, 26)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_NRZI)
        self.digital_correlate_access_code_tag_xx_1_1 = digital.correlate_access_code_tag_bb('01010101010101010101010101111110', 2, "frame_start")
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_wavfile_source_0 = blocks.wavfile_source('../iq/iq_1765716233.wav', False)
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tag_debug_1 = blocks.tag_debug(gr.sizeof_char*1, "Ais Detector", "frame_start")
        self.blocks_tag_debug_1.set_display(True)
        self.blocks_message_debug_1 = blocks.message_debug(True, gr.log_levels.debug)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate_resample/(pi*ais_bitrate)))


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.blocks_message_debug_1, 'print'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.qtgui_time_sink_x_2_0_1_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_1_1, 0), (self.blocks_tag_debug_1, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_correlate_access_code_tag_xx_1_1, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_hdlc_deframer_bp_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_waterfall_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "read_bin_iq")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_resampling_koeff(self.samp_rate/(4*self.ais_bitrate))
        self.set_samp_rate_resample(self.samp_rate/self.resampling_koeff)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth_ais/2, self.transition_bw))
        self.qtgui_time_sink_x_2_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq_center, self.samp_rate)

    def get_ais_bitrate(self):
        return self.ais_bitrate

    def set_ais_bitrate(self, ais_bitrate):
        self.ais_bitrate = ais_bitrate
        self.set_ais_fsk_deviation_hz(self.ais_modulation_index * self.ais_bitrate / 2)
        self.set_resampling_koeff(self.samp_rate/(4*self.ais_bitrate))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate_resample/(self.pi*self.ais_bitrate)))
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.gaussian(gain=1.0, spb=self.samp_rate_resample / self.ais_bitrate,bt=0.4, ntaps=int(self.filter_span*self.samp_rate_resample / self.ais_bitrate)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_resample, (0.6*self.ais_bitrate), (0.5*self.ais_fsk_deviation_hz), window.WIN_HAMMING, 1.0))

    def get_resampling_koeff(self):
        return self.resampling_koeff

    def set_resampling_koeff(self, resampling_koeff):
        self.resampling_koeff = resampling_koeff
        self.set_samp_rate_resample(self.samp_rate/self.resampling_koeff)

    def get_ais_modulation_index(self):
        return self.ais_modulation_index

    def set_ais_modulation_index(self, ais_modulation_index):
        self.ais_modulation_index = ais_modulation_index
        self.set_ais_fsk_deviation_hz(self.ais_modulation_index * self.ais_bitrate / 2)

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth_ais/2, self.transition_bw))

    def get_samp_rate_resample(self):
        return self.samp_rate_resample

    def set_samp_rate_resample(self, samp_rate_resample):
        self.samp_rate_resample = samp_rate_resample
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate_resample/(self.pi*self.ais_bitrate)))
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.gaussian(gain=1.0, spb=self.samp_rate_resample / self.ais_bitrate,bt=0.4, ntaps=int(self.filter_span*self.samp_rate_resample / self.ais_bitrate)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_resample, (0.6*self.ais_bitrate), (0.5*self.ais_fsk_deviation_hz), window.WIN_HAMMING, 1.0))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.freq_low_ais, self.samp_rate_resample)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate_resample/(self.pi*self.ais_bitrate)))

    def get_freq_low_ais(self):
        return self.freq_low_ais

    def set_freq_low_ais(self, freq_low_ais):
        self.freq_low_ais = freq_low_ais
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.freq_low_ais, self.samp_rate_resample)

    def get_freq_high_ais_0(self):
        return self.freq_high_ais_0

    def set_freq_high_ais_0(self, freq_high_ais_0):
        self.freq_high_ais_0 = freq_high_ais_0

    def get_freq_center(self):
        return self.freq_center

    def set_freq_center(self, freq_center):
        self.freq_center = freq_center
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq_center, self.samp_rate)

    def get_filter_span(self):
        return self.filter_span

    def set_filter_span(self, filter_span):
        self.filter_span = filter_span
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.gaussian(gain=1.0, spb=self.samp_rate_resample / self.ais_bitrate,bt=0.4, ntaps=int(self.filter_span*self.samp_rate_resample / self.ais_bitrate)))

    def get_bandwidth_ais(self):
        return self.bandwidth_ais

    def set_bandwidth_ais(self, bandwidth_ais):
        self.bandwidth_ais = bandwidth_ais
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.bandwidth_ais/2, self.transition_bw))

    def get_ais_fsk_deviation_hz(self):
        return self.ais_fsk_deviation_hz

    def set_ais_fsk_deviation_hz(self, ais_fsk_deviation_hz):
        self.ais_fsk_deviation_hz = ais_fsk_deviation_hz
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_resample, (0.6*self.ais_bitrate), (0.5*self.ais_fsk_deviation_hz), window.WIN_HAMMING, 1.0))




def main(top_block_cls=read_bin_iq, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
