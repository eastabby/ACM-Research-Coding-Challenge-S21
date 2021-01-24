from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

# SEQRECORD OBJECT read in from file
record = SeqIO.read("Genome.gb", "genbank")

# CREATE EMPTY DIAGRAM, TRACK, FEATURE SET
gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# Take each GENE SeqFeature object in SeqRecord >> feature on diagram
for feature in record.features:
    if feature.type != "gene":
        # Exclude it
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.palevioletred
    else:
     color = colors.cornflowerblue
    gd_feature_set.add_feature(
        feature, sigil = "ARROW", arrowshaft_height = .8, color = color, label = True, label_size = 15
    )

# Checking for common enzyme recognition sites
for site, name, color in [("GAATTC","EcoRI",colors.darkslategray),
                          ("GGGCCC	","EcoRI",colors.yellow),
                          ("ACCGGT	","Agel Agel-HF",colors.lightpink),
                          ("CCCGGG","SmaI",colors.blueviolet),
                          ("AAGCTT","HindIII",colors.darkred),
                          ("GGATCC","BamHI",colors.purple)]:
    index = 0
    while True:
        index  = record.seq.find(site, start=index)
        if index == -1 : break
        feature = SeqFeature(FeatureLocation(index, index+len(site)))
        gd_feature_set.add_feature(feature, sigil = "BOX", color=color, name=name,
                                   label=True, label_size = 15,
                                   label_color=color)
        index += len(site)

# create shape using reportlab objects
gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(25 * cm, 25 * cm),
    start=0,
    end=len(record),
    circle_core=0.7,
)
# render shapes
gd_diagram.write("circle.png", "PNG")






