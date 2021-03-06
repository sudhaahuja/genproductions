
import FWCore.ParameterSet.Config as cms


from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(9.9),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
		'MSEL=39                  ! All SUSY processes ',
		'IMSS(1) = 11             ! Spectrum from external SLHA file',
		'IMSS(11) = 1             ! Make gravitino the LSP', 
		'IMSS(21) = 33            ! LUN number for SLHA File (must be 33) ',
		'IMSS(22) = 33            ! Read-in SLHA decay table '),
        SLHAParameters = cms.vstring('SLHAFILE = Configuration/Generator/data/StealthSbottomTo3b_M200_Mf100_Ms90.slha'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters','SLHAParameters')
    )
)
