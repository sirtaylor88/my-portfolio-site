from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from portfolio.models import Publication

import datetime
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# python manage.py seeds --mode=refresh

""" Clear all data and reseed """
MODE_REFRESH = "refresh"

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")

def clear_data():
    """Deletes all the table data"""
    logger.info("Deleting Publication instances...")
    Publication.objects.all().delete()

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    logger.info("Creating publications...")

    publication_1 = Publication(
        title            = "Thermodynamics of faceted palladium(-gold) nanoparticle supported on rutile titania nanorods studied by transmission electron microscopy",
        description      = "Many physical properties of nanoparticles (NPs) are driven by their equilibrium shape (ES). Thus, knowing the kinetic and thermodynamic parameters that affect the particle morphology is key for the rational design of NPs with targeted properties. Here, we report on the thermodynamic ES of supported monometallic palladium and bimetallic palladium–gold (Pd–Au) single-crystalline truncated nano-octahedra (TOs) studied using aberration-corrected transmission electron microscopy (TEM). Monometallic palladium and bimetallic Pd62Au38 and Pd43Au57 TOs were grown by pulsed laser deposition on rutile titania (r-TiO2) nanorods exposing mainly (110) facets. Particle structure and dimension were first obtained from aberration-corrected high resolution TEM (HRTEM) images acquired parallel to the metal–oxide interface. By fitting an extended Wulff–Kaishev rule to the HRTEM data of the truncated octahedral thermodynamic ES in the size range of 2 to 5 nm, we secondly determined the interface and excess line energies associated with the particle–oxide–vacuum triple phase junction in Pd and Pd43Au57 TOs in the epitaxial relationship Pd(–Au)(111)〈101〉‖r-TiO2(110)[1−1−1] and in Pd62Au38 TOs in the epitaxial relationship Pd62Au38(100)〈101〉‖r-TiO2(110)[1−10]. Our results show a decrease in particle adhesion to the oxide support upon alloying Pd with Au. The loss in adhesion is tentatively attributed to an increase of the lattice strain induced at the metal–oxide interface as gold atoms are added to the palladium lattice.",
        authors          = ["Nhat Tai Nguyen", "Jaysen Nelayah", "Damien Alloyeau", "Guillaume Wang", "Laurent Piccolo", "Pavel Afanasiev", "Christian Ricolleau"],
        publisher        = "Physical Chemistry Chemical Physics",
        publication_date = datetime.datetime(2018, 4, 5),
        link             = "https://doi.org/10.1039/C8CP00737C",
        cover_image      = ImageFile(open("portfolio/static/images/pubs/pccp_issue_18.jpg", "rb"), name = "pccp_issue_18.jpg")
    )
    publication_1.save()

    publication_2 = Publication(
      title            = "Structural Properties of Catalytically Active Bimetallic Gold–Palladium Nanoparticles Synthesized on Rutile Titania Nanorods by Pulsed Laser Deposition",
      description      = "Gold–palladium nanoparticles with an average size of 3.5 nm and controlled compositions were grown on rutile titania nanorods using pulsed laser deposition. The structural properties of the as-synthesized nanoparticles and their interface with the oxide support were studied at the atomic scale using aberration-corrected transmission electron microscopy (TEM). High resolution TEM imaging showed that both polycrystalline Au–Pd particles with droplet morphology and single-crystalline particles with truncated octahedron morphology were stabilized on the nanorods during laser deposition depending on the degree of epitaxy between the nanoparticles and the oxide support. By analyzing the single-crystalline particles formed in the presence of a strong epitaxy, 11 epitaxial relationships between the Au–Pd nanoparticles and their support were identified with the two dominant ones being: Au–Pd (111) [101] // r-TiO2(110) [11̅1̅] and Au–Pd (100) [101] // r-TiO2 (110) [11̅0]. Catalytic testing of the bimetallic titania-supported Au–Pd nanoparticles in the partial hydrogenation of 1,3-butadiene showed that they were both active and selective for this reaction. An increase in the catalytic stability with the gold content was evidenced.",
      authors          = ["Nhat Tai Nguyen", "Jaysen Nelayah", "Pavel Afanasiev", "Laurent Piccolo", "Damien Alloyeau", "Christian Ricolleau"],
      publisher        = "Crystal Growth & Design",
      publication_date = datetime.datetime(2017, 10, 17),
      link             = "https://doi.org/10.1021/acs.cgd.7b00708",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/crystal_growth_design_vol_18_issue_1.jpg", "rb"), name = "crystal_growth_design_vol_18_issue_1.jpg")
    )
    publication_2.save()

    publication_3 = Publication(
      title            = "Ostwald-Driven Phase Separation in Bimetallic Nanoparticle Assemblies",
      description      = "The compositional stability of bimetallic nanoparticles (NPs) is crucial for many applications. We have studied the coarsening of amorphous carbon-supported Au–Pd NPs during annealing at 873 K. Using scanning transmission electron microscopy and energy-dispersive spectroscopy measurements, we show that, despite a complete miscibility of the two metals, the particle assembly undergoes a phase separation during annealing, which leads to two distinct populations: Au-rich NPs with a mean radius of 3.5 nm and large Pd-rich NPs with a mean radius of 25 nm. Thermodynamic calculations and kinetic Monte Carlo simulations explain this behavior that is driven by the competition between surface and mixing energy and by the different mobilities of the two atomic species.",
      authors          = ["Geoffroy Prévot", "Nhat Tai Nguyen", "Damien Alloyeau", "Christian Ricolleau", "Jaysen Nelayah"],
      publisher        = "ACS Nano",
      publication_date = datetime.datetime(2016, 3, 18),
      link             = "https://doi.org/10.1021/acsnano.5b07377",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/acs_nano_vol_10_issue_4.jpg", "rb"), name = "acs_nano_vol_10_issue_4.jpg")
    )
    publication_3.save()

    publication_4 = Publication(
      title            = "Au–Rh and Au–Pd nanocatalysts supported on rutile titania nanorods: structure and chemical stability",
      description      = "Au, Rh, Pd, Au–Rh and Au–Pd nanoparticles (NPs) were synthesized by colloidal chemical reduction and immobilized on hydrothermally-prepared rutile titania nanorods. The catalysts were characterized by aberration-corrected TEM/STEM, XPS, and FTIR, and were evaluated in the hydrogenation of tetralin in the presence of H2S. Oxidizing and reducing thermal treatments were employed to remove the polyvinyl alcohol (PVA) surfactant. Reduction in H2 at 350 °C was found efficient for removing the PVA while preserving the size (ca. 3 nm), shape and bimetallic nature of the NPs. While Au–Pd NPs are alloyed at the atomic scale, Au–Rh NPs contain randomly distributed single-phase domains. Calcination–reduction of Au–Rh NPs mostly leads to separated Au and Rh NPs, while pre-reduction generates a well-defined segregated structure with Rh located at the interface between Au and TiO2 and possibly present around the NPs as a thin overlayer. Both the titania support and gold increase the resistance of Rh and Pd to oxidation. Furthermore, although detrimental to tetralin hydrogenation initial activity, gold stabilizes the NPs against surface sulfidation in the presence of 50 ppm H2S, leading to increased catalytic performances of the Au–Rh and Au–Pd systems as compared to their Rh and Pd counterparts.",
      authors          = ["Jaysen Nelayah", "Nhat Tai Nguyen", "Damien Alloyeau", "Guillaume Wang", "Christian Ricolleau"],
      publisher        = "Physical Chemistry Chemical Physics",
      publication_date = datetime.datetime(2014, 7, 3),
      link             = "https://doi.org/10.1039/C4NR01427H",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/pccp_issue_42.jpg", "rb"), name = "pccp_issue_42.jpg")
    )
    publication_4.save()

    publication_5 = Publication(
      title            = "Long-range chemical orders in Au–Pd nanoparticles revealed by aberration-corrected electron microscopy",
      description      = "Despite the importance of gold–palladium nanoalloys in heterogeneous catalysis, the phase stability of Au–Pd alloys still remains unclear. We report here on the alloying and chemical ordering in epitaxially-grown and post-annealed gold–palladium nanoparticles (NPs) using aberration-corrected transmission electron microscopy. Au–Pd NPs with a controlled size, composition and structure were grown by pulsed laser deposition on freshly-cleaved NaCl(001) single crystals heated at 300 °C. After transfer to an amorphous carbon support, the NPs were annealed in vacuum at elevated temperatures above 400 °C for a few hours (6–10 hours) to promote chemical ordering. The as-grown NPs were mostly monocrystalline with a chemically-disordered face-centered cubic structure. Upon high-temperature annealing, a high degree of chemical ordering was observed in nanometer-sized NPs. Electron microscopy measurements showed that both L10 and L12 orders are stabilized in the Au-rich region of the Au–Pd phase diagram. These ordered phases exist at temperatures as high as 600 °C. Moreover, compositional analysis of single annealed particles revealed that the observed chemical ordering occurs in parallel to a two-tiered Ostwald ripening process. Due to this ripening process, a clear dependence between chemical composition and particle size is established during annealing with an enrichment in Pd as the NPs grow in size. Our results, besides clarifying some controversial aspects about long-range order in Au–Pd alloys, shed light on the structural stability of Au–Pd nanoalloys at elevated temperatures.",
      authors          = ["Zere Konuspayeva", "Pavel Afanasiev", "Thanh-Son Nguyen", "Luca Di Felice", "Franck Morfin", "Nhat Tai Nguyen", "Jaysen Nelayah", "Christian Ricolleau", "Z. Y. Li", "Jun Yuan", "Gilles Berhault", "Laurent Piccolo"],
      publisher        = "Nanoscale",
      publication_date = datetime.datetime(2015, 3, 6),
      link             = "https://doi.org/10.1039/C5CP00249D",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/nanoscale_issue_17.jpg", "rb"), name = "nanoscale_issue_17.jpg")
    )
    publication_5.save()

    publication_6 = Publication(
      title            = "Nanoalloying bulk-immiscible iridium and palladium inhibits hydride formation and promotes catalytic performances",
      description      = "The hydrogen sorption properties of oxide-supported Ir–Pd nanoalloys have been determined for the first time, and correlated with their catalytic behavior. The addition of Ir to Pd suppresses hydride formation and leads to improved catalytic performances with respect to pure metals in the preferential oxidation of CO in H2 excess (PROX).",
      authors          = ["Claudia Zlotea", "Franck Morfin", "Thanh-Son Nguyen", "Nhat Tai Nguyen", "Jaysen Nelayah", "Christian Ricolleau", "M. Latroche", "Laurent Piccolo"],
      publisher        = "Nanoscale",
      publication_date = datetime.datetime(2014, 6, 26),
      link             = "https://doi.org/10.1039/C4NR02836H",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/nanoscale_issue_17.jpg", "rb"), name = "nanoscale_issue_17.jpg")
    )
    publication_6.save()

    publication_7 = Publication(
      title            = "Structural and Optical Properties of Annealed Porous Silicon Bragg Reflector for Thin-Film Crystalline Silicon Solar Cells",
      description      = "The hydrogen sorption properties of oxide-supported Ir–Pd nanoalloys have been determined for the first time, and correlated with their catalytic behavior. The addition of Ir to Pd suppresses hydride formation and leads to improved catalytic performances with respect to pure metals in the preferential oxidation of CO in H2 excess (PROX).",
      authors          = ["Maïlys Grau", "Nhat Tai Nguyen", "Alain Straboni", "Mustapha Lemiti"],
      publisher        = "Energy Procedia",
      publication_date = datetime.datetime(2011, 12, 23),
      link             = "https://doi.org/10.1016/j.egypro.2011.10.144",
      cover_image      = ImageFile(open("portfolio/static/images/pubs/energy_procedia_vol_10.gif", "rb"), name = "energy_procedia_vol_10.gif")
    )
    publication_7.save()

    return


