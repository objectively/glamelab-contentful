
from contentful_cma_client import client, SPACE_ID, CONTENTFUL_ENV

lorem_ipsum = '## Heading (level 2) \nLorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lobortis dignissim turpis vitae efficitur. Nulla quis semper mi. Vivamus maximus risus quis velit gravida, nec porta ipsum malesuada. Morbi sed facilisis purus. Nam consequat consequat ex sed ornare. Vivamus at est posuere, posuere risus commodo, accumsan nunc. Ut sollicitudin arcu nec nisi aliquet semper. Quisque fringilla nunc sit amet scelerisque viverra. Aliquam euismod mi id justo fringilla, sit amet lobortis elit convallis.\n\nOrci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc venenatis euismod sagittis. Nam gravida non massa sit amet gravida. Etiam at volutpat mi. Praesent gravida imperdiet lobortis. Aenean nec posuere nunc, id congue ex. Aliquam quis justo congue, bibendum quam eu, congue ante. Praesent enim est, sodales sit amet sagittis id, feugiat eget nulla. Morbi vitae massa eget lacus dapibus tincidunt ac eu ex. Curabitur sit amet pellentesque mauris. In dictum nec erat tincidunt porttitor. Vivamus maximus tortor lacus, a dapibus lorem pharetra et. Morbi fringilla tortor vel ipsum commodo ornare. Mauris rhoncus congue quam quis accumsan.'

def update_institution_description(entry_id, description):
    # get entry 
    entry = client.entries(SPACE_ID, CONTENTFUL_ENV).find(entry_id)
    # update the Entry:
    entry.institution_description = description
    # save the entry 
    entry.save()
    # publish entry 
    # entry.publish()

update_institution_description('0ff24b61bb87495c9a6cc45f40bac09b', lorem_ipsum)