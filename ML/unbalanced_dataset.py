def unbalanced_dataset(dataset):
    target_0 = dataset[dataset['target'] == 0] # veri setindeki target değeri 0 olanları getir
    target_0_removed = target_0.sample(n=300)  # sınıfı 0 olanlardan rastgele 200 tane seç

    new_dataset = dataset.drop(target_0_removed.index) # yeni veri seti

    return new_dataset