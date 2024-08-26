from ROOT import TFile,TH1F,TH2F,TCanvas,gPad,TLatex,TLegend,TPad,TLine,THStack,TGraph, TH1D, gPad
from ROOT import TColor
from math import sqrt,log
import numpy as np

###################################################
##         Drawing Utilities
###################################################

def DrawFrame(xmin, xmax, ymin, ymax, Title, setMargins):

    if setMargins:
      gPad.SetLeftMargin(0.2)
      gPad.SetRightMargin(0.05)
      gPad.SetBottomMargin(0.1)
      gPad.SetTopMargin(0.05)

    frame = gPad.DrawFrame(xmin,ymin,xmax,ymax)
    frame.SetTitle(Title)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetXaxis().SetTitleSize(0.06)
    frame.GetYaxis().SetTitleSize(0.06)
    frame.GetXaxis().SetTitleOffset(0.8)
    frame.GetYaxis().SetTitleOffset(1.3)
    frame.GetXaxis().CenterTitle()
    frame.GetYaxis().CenterTitle()
    gPad.SetTicks(1,1)
    return frame

def SetMarkerStyle(hist, style, color, alpha, size):
    hist.SetMarkerStyle(style)
    hist.SetMarkerColorAlpha(color, alpha)
    hist.SetMarkerSize(size)

def SetLineStyle(hist, style, color, alpha, width):
    hist.SetLineStyle(style)
    hist.SetLineColorAlpha(color, alpha)
    hist.SetLineWidth(width)

def SetFillStyle(hist, style, color, alpha):
    hist.SetFillStyle(style)
    hist.SetFillColorAlpha(color, alpha)
def style_frame(frame):
    frame.GetYaxis().SetLabelFont(43)
    frame.GetYaxis().SetTitleFont(43)
    frame.GetYaxis().SetLabelSize(28)
    frame.GetYaxis().SetTitleSize(28)
    frame.GetYaxis().SetTitleOffset(1.5)
    frame.GetYaxis().SetNdivisions(505)
    
    frame.GetXaxis().SetLabelFont(43)
    frame.GetXaxis().SetTitleFont(43)
    frame.GetXaxis().SetLabelSize(28)
    frame.GetXaxis().SetTitleSize(40)
    frame.GetXaxis().SetTitleOffset(1.0)
    frame.GetXaxis().SetNdivisions(505)
    
###################################################
##          2D Histogram Plot
###################################################

f1 = TFile('./ForSmearingHYDLHC_2024Response5036_d20240602_v1.root', "READ")
f1.cd();
HF_vs_Npart = f1.Get("SmearingHist/HF_vs_Npart_0");

c1 = TCanvas("c1", "c1", 800, 800);
c1.cd()
p1 = TPad("p1", "p1", 0., 0., 1., 1.)
p1.SetLeftMargin(0.12)
p1.SetRightMargin(0.12)
p1.SetBottomMargin(0.12)
p1.SetTopMargin(0.1)
p1.Draw()
p1.cd()

title = ";N_{part};HF"
frame1 = DrawFrame(0, 450, 0, 7000, title, False)
style_frame(frame1)
frame1.GetXaxis().SetTitleSize(35)

HF_vs_Npart.SetStats(False);
HF_vs_Npart.Draw("Same colz");

Tl = TLatex()
s1 = "Centrality 0-100%"
s2 = "#it{Preliminary} "
s3 = "PbPb HYD (5.36 TeV)"
s4 = "#bf{CMS} "

Tl.SetNDC()
Tl.SetTextFont(43)
Tl.SetTextSize(25)
Tl.DrawLatex(0.25,0.70, s1)
Tl.DrawLatex(0.2,0.92, s2)
Tl.DrawLatex(0.25,0.65, s3)

T2=TLatex()
T2.SetNDC()
T2.SetTextFont(43)
T2.SetTextSize(25)
T2.DrawLatex(0.12,0.92, s4)

c1.SaveAs("HFnpart2D.pdf")

###################################################
##          1D Histograms Plot
###################################################

HF_npart_20=HF_vs_Npart.ProjectionY("HF_npart_20", 20, 21);
HF_npart_100=HF_vs_Npart.ProjectionY("HF_npart_100", 100, 101);
HF_npart_200=HF_vs_Npart.ProjectionY("HF_npart_200", 200, 201);
HF_npart_300=HF_vs_Npart.ProjectionY("HF_npart_300", 300, 301);

HF_npart_20 = HF_npart_20.Rebin(int(HF_npart_20.GetNbinsX() / 100));
HF_npart_100 = HF_npart_100.Rebin(int(HF_npart_100.GetNbinsX() / 100));
HF_npart_200 = HF_npart_200.Rebin(int(HF_npart_200.GetNbinsX() / 100));
HF_npart_300 = HF_npart_300.Rebin(int(HF_npart_300.GetNbinsX() / 100));

HF_npart_20.Sumw2()
HF_npart_100.Sumw2()
HF_npart_200.Sumw2()
HF_npart_300.Sumw2()

HF_npart_20.Scale(1.0 /HF_npart_20.Integral("width"))
HF_npart_100.Scale(1.0 /HF_npart_100.Integral("width"))
HF_npart_200.Scale(1.0 /HF_npart_200.Integral("width"))
HF_npart_300.Scale(1.0 /HF_npart_300.Integral("width"))

SetMarkerStyle(HF_npart_20, 20, 633, 1, 1.3)
SetLineStyle(HF_npart_20, 1, 633, 1, 1)

SetMarkerStyle(HF_npart_100, 20, 610, 1, 1.3)
SetLineStyle(HF_npart_100, 1, 610, 1, 1)

SetMarkerStyle(HF_npart_200, 20, 801, 1, 1.3)
SetLineStyle(HF_npart_200, 1, 801, 1, 1)

SetMarkerStyle(HF_npart_300, 20, 410, 1, 1.3)
SetLineStyle(HF_npart_300, 1, 410, 1, 1)

c2 = TCanvas("c2", "c2", 800, 800);
c2.cd()
p1 = TPad("p1", "p1", 0., 0., 1., 1.)
p1.SetLeftMargin(0.12)
p1.SetRightMargin(0.12)
p1.SetBottomMargin(0.12)
p1.SetTopMargin(0.1)
p1.SetLogy()
p1.Draw()
p1.cd()

title = ";HF;Event Fraction"
frame1 = DrawFrame(0, 6000, 1e-5, 1e-1, title, False)
style_frame(frame1)
frame1.GetXaxis().SetTitleSize(35)

HF_npart_20.SetStats(False);
HF_npart_20.Draw("P same");
HF_npart_100.SetStats(False);
HF_npart_100.Draw("P same");
HF_npart_200.SetStats(False);
HF_npart_200.Draw("P same");
HF_npart_300.SetStats(False);
HF_npart_300.Draw("P same");

Tl = TLatex()
s1 = "Centrality 0-100%"
s2 = "#it{Preliminary} "
s3 = "PbPb HYD (5.36 TeV)"
s4 = "#bf{CMS} "

Tl.SetNDC()
Tl.SetTextFont(43)
Tl.SetTextSize(25)
Tl.DrawLatex(0.25,0.70, s1)
Tl.DrawLatex(0.2,0.92, s2)
Tl.DrawLatex(0.25,0.65, s3)

T2=TLatex()
T2.SetNDC()
T2.SetTextFont(43)
T2.SetTextSize(25)
T2.DrawLatex(0.12,0.92, s4)

c2.SaveAs("HFnpart1D.pdf")
