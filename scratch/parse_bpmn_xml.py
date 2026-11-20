import xml.etree.ElementTree as ET

def parse_bpmn(file_path):
    print(f"=== PARSING {file_path} ===")
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # namespaces
    ns = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}
    
    # find collaboration, participants (pools)
    collab = root.find('.//bpmn:collaboration', ns)
    if collab is not None:
        participants = collab.findall('bpmn:participant', ns)
        print("Participants / Pools:")
        for p in participants:
            print("  - Pool:", p.attrib.get('name', 'Unnamed'), "id:", p.attrib.get('id'))
    
    # find processes
    processes = root.findall('.//bpmn:process', ns)
    for proc in processes:
        proc_id = proc.attrib.get('id')
        print(f"\nProcess {proc_id}:")
        
        # lanes
        lanes = proc.findall('.//bpmn:lane', ns)
        if lanes:
            print("  Lanes:")
            for l in lanes:
                print("    * Lane:", l.attrib.get('name', 'Unnamed'))
        
        # tasks
        tasks = proc.findall('.//bpmn:task', ns)
        user_tasks = proc.findall('.//bpmn:userTask', ns)
        service_tasks = proc.findall('.//bpmn:serviceTask', ns)
        send_tasks = proc.findall('.//bpmn:sendTask', ns)
        receive_tasks = proc.findall('.//bpmn:receiveTask', ns)
        all_tasks = tasks + user_tasks + service_tasks + send_tasks + receive_tasks
        print(f"  Total Tasks: {len(all_tasks)}")
        for t in all_tasks[:10]:
            print("    - Task:", t.attrib.get('name', 'Unnamed'))
            
        # gateways
        ex_gw = proc.findall('.//bpmn:exclusiveGateway', ns)
        par_gw = proc.findall('.//bpmn:parallelGateway', ns)
        inc_gw = proc.findall('.//bpmn:inclusiveGateway', ns)
        print(f"  Gateways: Exclusive={len(ex_gw)}, Parallel={len(par_gw)}, Inclusive={len(inc_gw)}")
        for g in ex_gw + par_gw:
            print("    - Gateway:", g.attrib.get('name', 'Unnamed'))
            
        # events
        start_ev = proc.findall('.//bpmn:startEvent', ns)
        end_ev = proc.findall('.//bpmn:endEvent', ns)
        inter_ev = proc.findall('.//bpmn:intermediateCatchEvent', ns) + proc.findall('.//bpmn:intermediateThrowEvent', ns)
        print(f"  Events: Start={len(start_ev)}, End={len(end_ev)}, Intermediate={len(inter_ev)}")
        for e in start_ev + end_ev:
            print("    - Event:", e.attrib.get('name', 'Unnamed'))
            
        # sequence flows
        seq_flows = proc.findall('.//bpmn:sequenceFlow', ns)
        print(f"  Sequence Flows: {len(seq_flows)}")

parse_bpmn('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/BPMN_As_Is_ARTHA.bpmn')
print("\n" + "="*50 + "\n")
parse_bpmn('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/BPMN_To_Be_ARTHA.bpmn')

