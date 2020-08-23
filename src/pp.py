import string
import re


def preprocessing_text(text):
    text = text.replace('&', 'and')
    for p in string.punctuation:
        text = text.replace(p, '')
    text = re.sub('RTL', 'register transfer level', text)
    text = re.sub('PSG', 'phrase structure grammars', text)
    text = re.sub('Quartus', 'software', text)
    text = re.sub('DefinitionofDone', 'Definition of Done', text)
    text = re.sub('DCDC', 'electronic circuit or electromechanical device', text)
    text = re.sub('AIML', 'AI machine learning', text)
    text = re.sub('IP', 'internet protocol', text)
    text = re.sub('DevOps', 'development and operation', text)
    text = re.sub('CONOPS', 'Concept of operation', text)
    text = re.sub('OWASP', 'Open Web Application Security Project', text)
    text = re.sub('SAP', 'electronic circuit or electromechanical device', text)
    text = re.sub('BPR', 'Business Process Re engineering', text)
    text = re.sub('CoE', 'Center of Excellence', text)
    text = re.sub('MLE', 'maximum likelihood estimate', text)
    text = re.sub('EMS', 'AElectronics Manufacturing Service', text)
    text = re.sub('IPs', 'Intrusion Prevention System', text)
    text = re.sub('ERP', 'Enterprise Resource Planning', text)
    text = re.sub('AR', 'Augmented Reality', text)
    text = re.sub('Gxp', 'Good x practice', text)
    text = re.sub('VoIP', 'Voice over Internet Protocol', text)
    text = re.sub('FAT', ' File Allocation Table', text)
    text = re.sub('API', 'Application Programming Interface', text)
    text = re.sub('CCM', 'Customer Communications Management', text)
    text = re.sub('OSEK', 'Open system together with interfaces for automotive electronics', text)
    text = re.sub('WBS', 'Work Breakdown Structure', text)
    text = re.sub('HVAC', 'heating, ventilating and air　conditioning', text)
    text = re.sub('SDKs', 'Software Development Kits', text)
    text = re.sub('GRC', 'Governance Risk and Compliance', text)
    text = re.sub('GLP', 'Good Laboratory Practice', text)
    text = re.sub('ETL', 'Extract Transform Load', text)
    text = re.sub('CRM', 'Customer Relationship Managemen', text)
    text = re.sub('PCT', 'Patent Cooperation Treaty', text)
    text = re.sub('SAN', 'Storage Area Network', text)
    text = re.sub('NMS', ' Network Management System', text)
    text = re.sub('HSE', 'Health Safety Environment', text)
    text = re.sub('AEB', 'Autonomous Emergency Brakings', text)
    text = re.sub('SME', 'Subject Matter Expert', text)
    text = re.sub('RFP', 'Request For Proposal', text)
    text = re.sub('NETCONF', 'Network Configuration Protocol', text)
    text = re.sub('PDU', 'Protocol Data Unit', text)
    text = re.sub('FMEA', 'Failure Mode and Effect Analysis', text)
    text = re.sub('CTQs', 'Critical To Quality', text)
    text = re.sub('DMA', 'Direct Memory Access', text)
    text = re.sub('OSHA', 'Occupational Safety and Health act', text)
    text = re.sub('VLANS', 'Virtual Local Area Network', text)
    text = re.sub('SDLC', 'Software Development Life Cycle', text)
    # text = re.sub('ADASAD','',text)
    text = re.sub('JDBC', 'Java Database Connectivity', text)
    text = re.sub('CPUGPU', 'CPU GPU', text)
    # text = re.sub('GNF',' ',text)
    text = re.sub('UML', 'Unified Modeling Language', text)
    # text = re.sub('CRPs','',text)
    text = re.sub('PCI', 'Peripheral Component Interconnect', text)
    text = re.sub('CLI', 'Common Language Infrastructure', text)
    # text = re.sub('TUB','',text)
    # text = re.sub('FMI','',text)
    # text = re.sub('SUI','',text)
    text = re.sub('IIS', 'Internet Information Services', text)
    # text = re.sub('HRSD','',text)
    # text = re.sub('PNC','',text)
    # text = re.sub('GSK','',text)
    text = re.sub('PCI', 'Peripheral Component Interconnect', text)
    # text = re.sub('GCR','',text)
    text = re.sub('KGIs', 'Key Goal Indicator', text)
    # text = re.sub('ASHRAE','',text)
    # text = re.sub('AHRI','',text)
    text = re.sub('TFS', 'Azure DevOps Server', text)
    text = re.sub('ASPNET', 'Active Server Pages NET', text)
    text = re.sub('CPM', 'Cost Per Mille', text)
    text = re.sub('NLP', 'Natural Language Processing', text)
    # text = re.sub('OFS','',text)
    # text = re.sub('DTCC','',text)
    # text = re.sub('PRS','',text)
    text = re.sub('MLAI', 'machine learning AI', text)
    text = re.sub('ESG', 'Environment Social Governance', text)
    # text = re.sub('DoD','',text)
    text = re.sub('Ops', 'operations', text)
    text = re.sub('CBA', 'Good Manufacturing Practice', text)
    # text = re.sub('GMP','',text)
    text = re.sub('CIO', 'Chief Information Officer ', text)
    text = re.sub('BOMs', ' Byte Order Mark', text)
    # text = re.sub('ITC','',text)
    # text = re.sub('TSSCI','',text)
    # text = re.sub('OPA','',text)
    # text = re.sub('BDS','',text)
    text = re.sub('HDFS', 'Hadoop Distributed File System', text)
    text = re.sub('CPV', 'Cost Per View', text)
    # text = re.sub('TM1','',text)
    # text = re.sub('DFM','',text)
    # text = re.sub('BWHANA','',text)
    text = re.sub('HTML5CSSJS', 'HTML5 CSS JS', text)
    text = re.sub('BPM', 'Business Process Management ', text)
    text = re.sub('RFI', 'Request For Information', text)
    text = re.sub('NLU', 'Natural language understanding', text)
    # text = re.sub('CABAIL','',text)
    # text = re.sub('MOPs','',text)
    text = re.sub('QAQC', 'quality assurance quality control', text)
    # text = re.sub('RASP','',text)
    text = re.sub('ISO', 'International Organization for Standardization', text)
    text = re.sub('SOP', 'Standard Operating Procedures', text)
    # text = re.sub('AFCO','',text)
    text = re.sub('LDA', 'Local Delivery Agent', text)
    text = re.sub('NMF', 'Nonnegative Matrix Factorization', text)
    text = re.sub('QMS', 'Quality Management System', text)
    # text = re.sub('MVR','',text)
    text = re.sub('CSSLP', 'Certified Secure Software Lifecycle Professional', text)
    # text = re.sub('GEWB','',text)
    # text = re.sub('CASS','',text)
    text = re.sub('CISA', 'Certified Information Systems Auditor', text)
    text = re.sub('CRISC', 'Certified in Risk and Information Systems Control', text)
    text = re.sub('SDL', 'Simple DirectMedia Layer', text)
    # text = re.sub('ISOFDA','',text)
    text = re.sub('PLC', 'programmable logic controller', text)
    text = re.sub('HMI', 'Human Machine Interface', text)
    text = re.sub('ISTQB', 'International Software Testing Qualifications Board', text)
    text = re.sub('RDBMSs', 'Relational DataBase Management System ', text)
    text = re.sub('HWSW', 'Hardware and Software', text)
    # text = re.sub('PCAFA','',text)
    # text = re.sub('AFCO','',text)
    # text = re.sub('SLASLO','',text)
    # text = re.sub('RESTful','',text)
    text = re.sub('DSPFPGA', 'DSP FPGA', text)
    text = re.sub('ESXi', 'VMware ESX', text)
    text = re.sub('AAC', 'Advanced Audio Coding ', text)
    text = re.sub('SEM', 'Search Engine Marketing', text)
    text = re.sub('CVE', ' Common Vulnerabilities and Exposure', text)

    text = text.strip().split()

    return text