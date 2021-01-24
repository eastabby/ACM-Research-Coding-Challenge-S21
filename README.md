# ACM Research Coding Challenge (Spring 2021)

## Process
Upon first reading the coding challenge, I was *completely* lost. I began by looking into what a GenBank file is, and from there I researched the other keywords in the problem. My first attempt to create a genome map would utilize rather obscure and difficult-to-install software, which I later realized was not the ideal way to go about the problem. Following that, I came across a Python library called Biopython. This was infinitely easier to use and implement, so I ended up using this to complete the coding challenge.

After a little bit more research, I found several thorough guides on how to use Biopython for particular purposes. Specifically, I used the GenomeDiagram module to create my final diagram. Creating a genome diagram from this point was rather simple. Before anything else, I read the gene sequence from Genome.gb into my program. From there, I began by creating an empty "diagram" object, followed by an empty track and empty feature set. These will be used to "house" the details of our particular gene sequence. Next, I created a loop that would go through the "features" of the gene sequence. Each feature labeled as a gene would be added to the feature set created earlier. Each gene would be assigned a color and formatted to look nice on the resulting diagram. 

In addition to simply mapping the genes, I checked for common enzyme reception sites in the gene sequence. If a segment of the gene sequence was found to match that of the enzyme reception site, a thin line would pierce the diagram in a location that corresponds to where the reception site was located in the genome. In other words, it places a marker on the site of an area of interest on the genome, if one is found.

Finally, the contents of the diagram is complete. All that is left to do is draw the diagram and display it as an image. I created the shape of the diagram using objects from reportlab. All of the features and genes that I wanted to display are saved within the GenomeDiagram object, so I did not have to display each gene individually. However, if I were to end the program here, the output would be a PDF file. As required by the challenge, I needed to make output this file as an image. I ran into one last predicament: when drawn by reportlab, the output was a PNG file. After a final brief round of research, I discovered that reportlab can be used with the Python Imaging Library (PIL) to display the output as a PNG image. To do this, I had to install one final library: Poppler. Reportlab created the PDF, Poppler modified this into a PNG image, and this PNG image was displayed by the final line of code.

The final displayed output, "circle.png", is a simple map of the genome. The genes are organized in a circular pattern in alternating shades of pink and blue. They are imaged as an arrow instead of the standard box. This is because the direction of the arrow indicates the direction of the coding sequence (CDS). While it is a small detail, it is important to know the direction of the genetic code when analyzing genomes, so I thought it would be a nice feature to add in. The thin labeled lines mark where enzyme recognition sites occur in the genome. Finally, each feature is labeled appropriately and color coded.

## Libraries Used
- reportlab https://www.reportlab.com/opensource/
- Biopython https://biopython.org/
- Poppler https://pypi.org/project/python-poppler/
- https://pillow.readthedocs.io/en/stable/

## Resources
- http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec346
- https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html
- https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html
- https://biopython.org/docs/1.75/api/Bio.SeqFeature.html