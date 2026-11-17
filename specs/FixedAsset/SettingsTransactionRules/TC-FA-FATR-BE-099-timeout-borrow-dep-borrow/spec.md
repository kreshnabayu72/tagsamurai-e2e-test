---
id: TC-FA-FATR-BE-099-timeout-borrow-dep-borrow
title: "Transaction timeout dan versi setting pada transaksi Borrow"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r5", "§Aturan Logika Modul#r30", "§Aturan Logika Modul#r31", "§Aturan Logika Modul#r32", "§Aturan Logika Modul#r40", "§8.1#r5", "§9.2#b128", "§9.2#b140", "§9.2#b201", "§9.2#b203", "§9.2#b205", "§9.2#b206", "§9.2#b207", "§9.2#b208", "§9.2#b213", "§9.2#b214", "§9.2#b217", "§9.2#b218", "§9.2#b219", "§9.2#b221", "§9.2#b222", "§9.2#b223", "§9.2#b225", "§9.2#b230", "§9.2#b231", "§9.2#b241", "§9.2#b242", "§9.2#b243", "§9.2#b244", "§9.2#b245", "§9.2#b246", "§9.2#b247", "§9.2#b248", "§9.2#b249", "§9.2#b251", "§9.2#b252", "§9.2#b253", "§9.2#b254", "§9.2#b255", "§9.2#b256", "§9.2#b257", "§9.2#b282", "§9.2#b288", "§9.2#b293", "§9.2#b294", "§9.2#b295", "§9.2#b300", "§9.2#b383", "§9.2#b395", "§9.2#b396", "§9.2#b436", "§9.2#b438", "§9.4.1#r11", "§9.4.2#r46", "§9.4.2#r135", "§9.4.2#r137", "§9.4.2#r148", "§9.4.2#r149", "§9.4.2#r150", "§9.4.2#r151", "§9.4.2#r152", "§9.4.3#b10", "§9.4.4#r37", "§9.6#r5", "§9.7#r2", "§9.7#r11", "§9.7#r22", "§9.7#r23", "§9.7#r24", "§9.7#r25", "§9.7#r26", "§9.7#r27", "§9.7#r31", "§9.10.1#b8", "§11#r21", "§11#r22", "§9.7#r29", "§9.8#r3", "§Aturan Logika Modul#r76"]
smoke: []
dependsOn:
  - "Borrow: pengajuan, Extension, dan Return"
trace:
  "§Aturan Logika Modul#r5": [2, 10, 20, 22, 23]
  "§Aturan Logika Modul#r30": [14]
  "§Aturan Logika Modul#r31": [5, 6, 37]
  "§Aturan Logika Modul#r32": [16, 18]
  "§Aturan Logika Modul#r40": [9, 11, 16]
  "§8.1#r5": [57, 96]
  "§9.2#b128": [27]
  "§9.2#b140": [9, 10]
  "§9.2#b201": [75]
  "§9.2#b203": [5, 55]
  "§9.2#b205": [5, 6, 7, 37, 46]
  "§9.2#b206": [5, 6, 40]
  "§9.2#b207": [46, 48]
  "§9.2#b208": [8, 41, 42, 43, 49]
  "§9.2#b213": [5, 55]
  "§9.2#b214": [6, 33, 56]
  "§9.2#b217": [74]
  "§9.2#b218": [32, 33, 70]
  "§9.2#b219": [32, 33]
  "§9.2#b221": [55, 56, 90, 91]
  "§9.2#b222": [55, 56]
  "§9.2#b223": [90, 91, 92]
  "§9.2#b225": [78]
  "§9.2#b230": [41]
  "§9.2#b231": [42]
  "§9.2#b241": [74]
  "§9.2#b242": [83]
  "§9.2#b243": [55, 56]
  "§9.2#b244": [55, 56, 101]
  "§9.2#b245": [59]
  "§9.2#b246": [58, 100]
  "§9.2#b247": [57]
  "§9.2#b248": [90, 91, 92]
  "§9.2#b249": [93, 94]
  "§9.2#b251": [7, 61, 62]
  "§9.2#b252": [6, 56]
  "§9.2#b253": [60]
  "§9.2#b254": [61, 62]
  "§9.2#b255": [63]
  "§9.2#b256": [64]
  "§9.2#b257": [65]
  "§9.2#b282": [74]
  "§9.2#b288": [11, 75]
  "§9.2#b293": [55, 56, 70]
  "§9.2#b294": [55, 56, 70]
  "§9.2#b295": [90, 91]
  "§9.2#b300": [55, 56, 70]
  "§9.2#b383": [2, 23, 51, 98]
  "§9.2#b395": [66, 70]
  "§9.2#b396": [70]
  "§9.2#b436": [9, 10, 11]
  "§9.2#b438": [5, 37, 46]
  "§9.4.1#r11": [29]
  "§9.4.2#r46": [74, 75]
  "§9.4.2#r135": [9, 10]
  "§9.4.2#r137": [5, 40, 46]
  "§9.4.2#r148": [55, 56]
  "§9.4.2#r149": [90, 91]
  "§9.4.2#r150": [74]
  "§9.4.2#r151": [56, 61, 62, 71]
  "§9.4.2#r152": [63]
  "§9.4.3#b10": [11]
  "§9.4.4#r37": [57, 61]
  "§9.6#r5": [73]
  "§9.7#r2": [5, 7, 8, 40, 41, 42, 43, 49]
  "§9.7#r11": [23, 51, 99]
  "§9.7#r22": [55]
  "§9.7#r23": [55, 56]
  "§9.7#r24": [90, 91]
  "§9.7#r25": [90, 91, 92]
  "§9.7#r26": [59, 93, 94]
  "§9.7#r27": [59, 93, 94]
  "§9.7#r31": [57]
  "§9.10.1#b8": [98, 99]
  "§11#r21": [74, 81, 83]
  "§11#r22": [55, 56, 70, 90, 91]
  "§9.7#r29": [90, 91, 92]
  "§9.8#r3": [61, 62, 63, 64, 65]
  "§Aturan Logika Modul#r76": [98]
owner: BE
---

# Transaction timeout dan versi setting pada transaksi Borrow

## Prerequisites
- Aktor: Rina Wulandari {runId} (Total Control) mengubah setting; Hana Pertiwi {runId} (Aktor Borrow) mengajukan atas nama Borrower; Rudi Hartono {runId} (Approver Borrow) menyetujui; Principal (operator Admin Console) mengubah status entitas, level plan, dan toggle Approval Workflow; Borrower sesuai entri data.
- Data:
  - DU-099-1: Entitas, Nama `Entitas Timeout Borrow {runId}`; entitas khusus spec ini.
  - DU-099-2: Group, Group `Gudang Utama {runId}`; Group tempat aset dipinjam.
  - DU-099-3: Group, Group `Gudang Cadangan {runId}`; Group untuk override cakupan dinamis.
  - DU-099-4: Category, Category `Alat Berat {runId}`, TAG Type `RFID`; Category aset yang dipinjam.
  - DU-099-5: User, Nama `Rina Wulandari {runId}`, Akses `Total Control`; Total Control yang mengubah setting.
  - DU-099-6: User, Nama `Hana Pertiwi {runId}`, Peran `Aktor Borrow`, Group `Gudang Utama {runId} beserta descendant dan Gudang Cadangan {runId}`; Aktor Borrow yang mengajukan atas nama Borrower.
  - DU-099-7: User, Nama `Rudi Hartono {runId}`, Peran `Approver Borrow`, Group `Gudang Utama {runId} beserta descendant`, Status `Active`; Approver Borrow.
  - DU-099-8: User, Nama `Bima Nugraha {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-9: User, Nama `Citra Dewi {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-10: User, Nama `Dedi Kurniawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-11: User, Nama `Eka Putri {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-12: User, Nama `Fitri Amelia {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-13: User, Nama `Gilang Ramadhan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-14: User, Nama `Hendra Gunawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-15: User, Nama `Indah Permatasari {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-16: User, Nama `Joko Susilo {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-17: User, Nama `Kirana Larasati {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Utama {runId}`; Borrower (Employee aktif).
  - DU-099-18: Setting Borrow, Max duration `14`, Due date reminders `D-3, D-1, D-day`; nilai default Company yang berlaku saat record sebelum perubahan diajukan.
  - DU-099-19: Setting Borrow, Max duration `5`, Due date reminders `D-day only`, Transaction timeout `10`; nilai Company yang diubah lewat Save Changes.
  - DU-099-20: Borrow, Borrower `Bima Nugraha {runId}`, Asset `Mesin Bor Meja Makita {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `4 hari`, Handover `T0`, Due date `T0 + 4 hari`, Max duration saat diajukan `14`, Due date reminders saat diajukan `D-3, D-1, D-day`; record sebelum perubahan: baris Borrowed berjalan yang diajukan pada nilai default.
  - DU-099-21: Borrow, Borrower `Citra Dewi {runId}`, Asset `Vibrator Beton Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `12 hari`, Due date `T0 + 12 hari`; baris aktif pertama Citra.
  - DU-099-22: Borrow, Borrower `Citra Dewi {runId}`, Asset `Mixer Beton Molen {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `12 hari`, Due date `T0 + 12 hari`; baris aktif kedua Citra.
  - DU-099-23: Borrow, Borrower `Citra Dewi {runId}`, Asset `Penggetar Beton Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `12 hari`, Due date `T0 + 12 hari`; baris aktif ketiga Citra.
  - DU-099-24: Borrow, Borrower `Dedi Kurniawan {runId}`, Asset `Genset Yanmar 10kVA {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Waiting for Approval`, Masuk status `T0`; baris Waiting for Approval yang masuk status pada T0, satu BRW dengan baris Borrowed berikutnya.
  - DU-099-25: Borrow, Borrower `Dedi Kurniawan {runId}`, Asset `Kompresor Udara Ingersoll {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`; baris Borrowed pada BRW yang sama dengan baris Waiting for Approval Dedi.
  - DU-099-26: Borrow, Borrower `Eka Putri {runId}`, Asset `Tangga Lipat Aluminium {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Waiting for Handover`, Masuk status `T0`; baris Waiting for Handover yang masuk status pada T0.
  - DU-099-27: Borrow, Borrower `Fitri Amelia {runId}`, Asset `Gerinda Besar Makita {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Waiting for Approval`, Masuk status `T0`; baris Waiting for Approval yang masuk status pada T0 dan disetujui pada T0 + 5 hari.
  - DU-099-28: Borrow, Borrower `Gilang Ramadhan {runId}`, Asset `Alat Ukur Jarak Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Draft`; baris Draft Borrow.
  - DU-099-29: Borrow, Borrower `Gilang Ramadhan {runId}`, Asset `Pompa Air Honda {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `10 hari`, Handover `T0`, Due date `T0 + 10 hari`; baris Borrowed yang bukan status menunggu.
  - DU-099-30: Borrow, Borrower `Hendra Gunawan {runId}`, Asset `Rangka Perancah Baja {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `12 hari`, Handover `T0`, Due date `T0 + 12 hari`, Extension `1 hari Waiting for Approval sejak T0`; baris Borrowed dengan Extension `1 hari` Waiting for Approval.
  - DU-099-31: Borrow, Borrower `Indah Permatasari {runId}`, Asset `Mesin Las Inverter {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Borrowed`, Duration `8 hari`, Handover `T0`, Due date `T0 + 8 hari`, Extension `1 hari menunggu review Aktor Borrow sejak T0`; baris Borrowed dengan Extension `1 hari` menunggu review Aktor Borrow.
  - DU-099-32: Asset, Asset `Mesin Potong Beton Husqvarna {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan sesudah Save Changes.
  - DU-099-33: Asset, Asset `Gergaji Rantai Stihl {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan pada Duration yang melebihi batas baru.
  - DU-099-34: Asset, Asset `Mesin Gerinda Tangan Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan setelah toggle Approval Workflow OFF.
  - DU-099-35: Asset, Asset `Pemadat Tanah Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Cadangan {runId}`, Status `Available`; aset yang ditambahkan ke Group Cadangan sesudah override dibuat.
  - DU-099-36: Asset, Asset `Troli Material Heavy Duty {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan di atas kuota.
  - DU-099-37: Asset, Asset `Bor Beton Hilti {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan pada level Basic yang menunggu approval.
  - DU-099-38: Asset, Asset `Scaffolding Set Lengkap {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan pada level Basic yang sudah disetujui.
  - DU-099-39: Borrow, Borrower `Joko Susilo {runId}`, Asset `Gergaji Rantai Stihl {runId}`, Duration `6 hari`; pengajuan yang ditolak karena Duration melebihi Max duration baru.
  - DU-099-40: Borrow, Borrower `Joko Susilo {runId}`, Asset `Mesin Potong Beton Husqvarna {runId}`, Duration `5 hari`; pengajuan sesudah perubahan yang tercatat dengan versi setting baru.
  - DU-099-41: Setting Borrow, Transaction timeout `9`; nilai Transaction timeout kedua yang disimpan pada T0 + 8 hari.
  - DU-099-42: Setting Borrow, Transaction timeout `2`; nilai Transaction timeout ketiga yang disimpan pada T0 + 8 hari dan membuat batas jatuh sebelum waktu Save.
  - DU-099-43: Override Group, Group `Gudang Cadangan {runId}`, Max duration `2`; override Group Gudang Cadangan yang dibuat sebelum aset Z1 ada di Group itu.
  - DU-099-44: Extension, Baris `Pompa Air Honda {runId}`, Durasi `3 hari`; Extension pada baris Borrowed yang total durasinya melebihi Max duration baru tetapi tidak melebihi Max duration saat diajukan.
  - DU-099-45: Asset, Asset `Gerobak Dorong Besi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Available`; aset untuk pengajuan setelah Save ketiga.
  - DU-099-46: Borrow, Borrower `Kirana Larasati {runId}`, Asset `Meja Kerja Lipat {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Utama {runId}`, Status `Draft`; baris Draft milik Borrower yang dinonaktifkan.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Timeout Borrow {runId}` yang tidak dipakai spec lain, sehingga perubahan setting, status, dan plan tidak menyentuh spec lain.
  - Level Feature Suite Borrowing bernilai `Full` dan Approval Workflow tersedia di plan entitas, kecuali diubah langkah.
  - Company default Borrow bernilai: Max duration `14`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Due date reminders `D-3, D-1, D-day`, Transaction timeout `7`, Require approval `ON`, Self service `OFF`, Duration unit `Days`, Auto-approve `OFF`.
  - Role Transaksi `Approver` untuk Borrow ditugaskan kepada Rudi Hartono {runId} pada Group `Gudang Utama {runId}` beserta descendant.
  - Override Asset untuk `Mesin Las Inverter {runId}` bernilai Require approval `OFF`.
  - Waktu acuan `T0` adalah waktu saat spec dimulai; waktu berlalu dinyatakan relatif terhadap `T0`, dan `T0 + 5 hari` dst. menurut zona waktu client.
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.

## Test Steps
### Record sebelum perubahan mencatat versi setting
1. Hana mencatat Max duration `14` dan Due date reminders `D-3, D-1, D-day` yang berlaku saat baris `Mesin Bor Meja Makita {runId}` milik Borrower `Bima Nugraha {runId}` diajukan, serta Versi setting yang tercatat pada baris itu
2. Verifikasi Versi setting yang dipakai evaluasi tercatat pada baris `Mesin Bor Meja Makita {runId}` sehingga dapat dibandingkan setelah setting berubah

### Save Changes menghitung ulang batas Transaction timeout dari waktu masuk status
3. Rina menyimpan Max duration bernilai `5`, Due date reminders bernilai `D-day only`, dan Transaction timeout bernilai `10`
4. Job batch penghitungan ulang batas Transaction timeout berjalan
5. Verifikasi batas Transaction timeout baris `Genset Yanmar 10kVA {runId}` (Waiting for Approval) menjadi `T0` ditambah 10 hari, yaitu waktu masuk status ditambah nilai baru dan bukan nilai lama
6. Verifikasi batas Transaction timeout baris `Tangga Lipat Aluminium {runId}` (Waiting for Handover) menjadi `T0` ditambah 10 hari, dan batas itu adalah batas pengambilan
7. Verifikasi batas Transaction timeout Extension pada baris `Rangka Perancah Baja {runId}` yang menunggu approval dan Extension pada baris `Mesin Las Inverter {runId}` yang menunggu review Aktor Borrow juga menjadi `T0` ditambah 10 hari
8. Verifikasi peringatan 1 hari tidak dikirim ulang untuk baris `Genset Yanmar 10kVA {runId}` dan `Tangga Lipat Aluminium {runId}` serta Extension `Rangka Perancah Baja {runId}` karena sisa waktu ke batas baru lebih dari 24 jam

### Save Changes tidak memengaruhi transaksi berjalan selain batas Transaction timeout
9. Verifikasi baris `Mesin Bor Meja Makita {runId}` tetap `Borrowed` dengan Duration `4 hari` dan Due date `T0 + 4 hari`
10. Verifikasi Max duration yang berlaku untuk baris `Mesin Bor Meja Makita {runId}` tetap `14` dan Due date reminders tetap `D-3, D-1, D-day` sesuai catatan, bukan nilai baru
11. Verifikasi baris `Pompa Air Honda {runId}` dengan Duration `10 hari` yang melebihi Max duration baru tetap `Borrowed` dan tidak dibatalkan otomatis
12. Waktu berlalu sampai `T0 + 1 hari`
13. Job harian pengingat Due date berjalan
14. Verifikasi pengingat D-3 baris `Mesin Bor Meja Makita {runId}` terkirim menurut Due date reminders yang di-snapshot saat diajukan walau nilai tersimpan kini `D-day only`

### Extension memakai snapshot transaksi asal
15. Hana mengajukan Extension `3 hari` pada baris `Pompa Air Honda {runId}` milik Borrower `Gilang Ramadhan {runId}`
16. Verifikasi Extension diterima karena total 13 hari tidak melebihi Max duration 14 pada snapshot baris asal, walau melebihi Max duration baru 5
17. Rudi menyetujui Extension baris `Pompa Air Honda {runId}`
18. Verifikasi Extension berstatus Approved dan Due date baris `Pompa Air Honda {runId}` menjadi T0 + 13 hari

### Pengajuan baru memakai aturan dan versi setting yang berlaku saat itu
19. Hana mengajukan Borrow aset `Gergaji Rantai Stihl {runId}` dengan Duration `6 hari` untuk Borrower `Joko Susilo {runId}`
20. Verifikasi pengajuan ditolak karena Duration melebihi Max duration baru 5
21. Hana mengajukan Borrow aset `Mesin Potong Beton Husqvarna {runId}` dengan Duration `5 hari` untuk Borrower `Joko Susilo {runId}`
22. Verifikasi pengajuan diterima karena Duration sama dengan Max duration baru
23. Verifikasi Versi setting yang tercatat pada baris `Mesin Potong Beton Husqvarna {runId}` lebih besar daripada Versi setting baris `Mesin Bor Meja Makita {runId}` sehingga transaksi sesudah Save mencatat versi setting baru

### Cakupan override dievaluasi dinamis terhadap data saat ini
24. Rina membuat override Group `Gudang Cadangan {runId}` dengan Max duration `2`
25. Rina menambahkan aset `Pemadat Tanah Wacker {runId}` di Category `Alat Berat {runId}` ke Group `Gudang Cadangan {runId}` sesudah override dibuat
26. Hana mengajukan Borrow aset `Pemadat Tanah Wacker {runId}` dengan Duration `3 hari` untuk Borrower `Bima Nugraha {runId}`
27. Verifikasi pengajuan ditolak karena Max duration `2` dari override Group berlaku untuk aset yang baru ada di Group itu, bukan snapshot saat override dibuat

### Kuota Max assets ditegakkan saat evaluasi
28. Hana mengajukan Borrow aset `Troli Material Heavy Duty {runId}` untuk Borrower `Citra Dewi {runId}` yang sudah punya 3 baris aktif
29. Verifikasi pengajuan ditolak karena kuota Max assets per borrower 3 sudah tercapai saat evaluasi

### Perpindahan status memulai hitungan lagi
30. Waktu berlalu sampai `T0 + 5 hari`
31. Rudi menyetujui pengajuan Borrow baris `Gerinda Besar Makita {runId}` milik Borrower `Fitri Amelia {runId}`
32. Verifikasi baris `Gerinda Besar Makita {runId}` berstatus `Waiting for Handover` dan hitungan Transaction timeout dimulai lagi sejak masuk status itu
33. Verifikasi batas Transaction timeout baris `Gerinda Besar Makita {runId}` adalah waktu masuk `Waiting for Handover` ditambah 10 hari, yaitu T0 + 15 hari dan bukan dihitung dari `T0`

### Batas lama terlewati tetapi batas baru belum tercapai
34. Waktu berlalu sampai `T0 + 8 hari`
35. Job timeout transaksi berjalan
36. Hana mencatat Due date baris `Rangka Perancah Baja {runId}` dan `Mesin Las Inverter {runId}` serta jumlah Extend baris `Rangka Perancah Baja {runId}`
37. Verifikasi baris `Genset Yanmar 10kVA {runId}`, `Tangga Lipat Aluminium {runId}`, `Gerinda Besar Makita {runId}`, dan Extension `Rangka Perancah Baja {runId}` serta `Mesin Las Inverter {runId}` masih menunggu karena batas lama 7 hari tidak dipakai lagi

### Save kedua mengirim ulang peringatan ketika sisa waktu 24 jam atau kurang
38. Rina menyimpan Transaction timeout bernilai `9`
39. Job batch penghitungan ulang batas Transaction timeout berjalan
40. Verifikasi batas Transaction timeout baris `Genset Yanmar 10kVA {runId}` dan `Tangga Lipat Aluminium {runId}` menjadi T0 + 9 hari, tepat 24 jam sesudah waktu Save
41. Verifikasi peringatan 1 hari dikirim ulang untuk baris `Genset Yanmar 10kVA {runId}` yang menunggu approval dan untuk Extension `Rangka Perancah Baja {runId}`
42. Verifikasi peringatan 1 hari dikirim ulang untuk baris `Tangga Lipat Aluminium {runId}` yang berstatus `Waiting for Handover`
43. Verifikasi peringatan 1 hari tidak dikirim ulang untuk baris `Gerinda Besar Makita {runId}` karena sisa waktu ke batas barunya lebih dari 24 jam

### Save ketiga menyetel batas yang jatuh sebelum waktu Save menjadi Save ditambah 24 jam
44. Rina menyimpan Transaction timeout bernilai `2`
45. Job batch penghitungan ulang batas Transaction timeout berjalan
46. Verifikasi batas Transaction timeout baris `Genset Yanmar 10kVA {runId}`, `Tangga Lipat Aluminium {runId}`, `Gerinda Besar Makita {runId}`, dan kedua Extension menjadi waktu Save ditambah 24 jam, bukan waktu masuk status ditambah 2 hari yang sudah lewat
47. Job timeout transaksi berjalan
48. Verifikasi tidak ada transaksi yang ditutup seketika saat Save: baris `Genset Yanmar 10kVA {runId}`, `Tangga Lipat Aluminium {runId}`, `Gerinda Besar Makita {runId}`, dan kedua Extension masih menunggu
49. Verifikasi peringatan 1 hari dikirim ulang untuk transaksi approval dan Waiting for Handover yang batasnya disetel ke waktu Save ditambah 24 jam, yaitu baris `Genset Yanmar 10kVA {runId}`, `Tangga Lipat Aluminium {runId}`, dan `Gerinda Besar Makita {runId}` serta Extension `Rangka Perancah Baja {runId}`
50. Hana mengajukan Borrow aset `Gerobak Dorong Besi {runId}` untuk Borrower `Hendra Gunawan {runId}`
51. Verifikasi Versi setting yang tercatat pada baris `Gerobak Dorong Besi {runId}` lebih besar daripada Versi setting baris `Mesin Potong Beton Husqvarna {runId}` karena ada Save sesudahnya
52. Principal mengubah status entitas menjadi `Suspended`

### Timeout menutup transaksi di entitas Suspended tanpa aktor
53. Waktu berlalu sampai 24 jam sesudah waktu Save ketiga, yaitu `T0 + 9 hari`
54. Job timeout transaksi berjalan
55. Verifikasi baris `Genset Yanmar 10kVA {runId}` yang menunggu approval ditutup oleh `System` sebagai `Canceled` dengan alasan `Timed out (Waiting for Approval)`, dan asetnya dikembalikan ke Draft baru tanpa nomor BRW, tanpa status Expired, walau entitas `Suspended`
56. Verifikasi baris `Tangga Lipat Aluminium {runId}` dan `Gerinda Besar Makita {runId}` yang berstatus `Waiting for Handover` ditutup oleh `System` sebagai `Canceled`, dan asetnya dikembalikan ke Draft baru tanpa nomor BRW, dengan alasan `Not picked up`
57. Verifikasi log transaksi memuat node `Canceled` pada BRW asal dan log aset dengan Modified By `System`
58. Verifikasi baris `Genset Yanmar 10kVA {runId}` tetap di BRW asal sebagai `Canceled`, dan BRW asal tidak berstatus `Canceled` karena baris `Kompresor Udara Ingersoll {runId}` masih `Borrowed`
59. Verifikasi Custody aset `Genset Yanmar 10kVA {runId}` dilepas dan status aset kembali `Available`
60. Verifikasi aturan no-show Borrow tidak berlaku: baris `Tangga Lipat Aluminium {runId}` tidak berstatus no-show
61. Verifikasi Extension baris `Rangka Perancah Baja {runId}` berstatus Canceled dengan Note `Timed out (Waiting for Approval)` dan Modified By `System`
62. Verifikasi Extension baris `Mesin Las Inverter {runId}` berstatus Canceled dengan Note `Timed out (Waiting for Review)` dan Modified By `System`
63. Verifikasi Due date baris `Rangka Perancah Baja {runId}` dan `Mesin Las Inverter {runId}` sama dengan catatan sehingga Extension yang ditutup tidak mengubah Due date pinjaman induk
64. Verifikasi baris `Rangka Perancah Baja {runId}` tetap `Borrowed` dan baris `Mesin Las Inverter {runId}` tetap `Overdue` karena Due date sudah lewat
65. Verifikasi jumlah Extend baris `Rangka Perancah Baja {runId}` sama dengan catatan sehingga tidak bertambah
66. Verifikasi baris `Gerobak Dorong Besi {runId}` masih menunggu approval karena baru 24 jam dari 2 hari sejak masuk status
67. Principal mengubah status entitas menjadi `Expired`

### Timeout N hari adalah N kali 24 jam di entitas Expired
68. Waktu berlalu sampai 48 jam sesudah baris `Gerobak Dorong Besi {runId}` masuk status Waiting for Approval, yaitu `T0 + 10 hari`
69. Job timeout transaksi berjalan
70. Verifikasi baris `Gerobak Dorong Besi {runId}` ditutup oleh `System` sebagai `Canceled` tepat saat batas 2 x 24 jam tercapai, dan asetnya dikembalikan ke Draft baru tanpa nomor BRW walau entitas `Expired`
71. Verifikasi alasan baris `Gerobak Dorong Besi {runId}` tercatat `Timed out (Waiting for Approval)`
72. Job timeout transaksi berjalan kembali
73. Verifikasi baris `Genset Yanmar 10kVA {runId}` yang sudah `Canceled` tidak diproses lagi: node `Canceled` pada log tetap satu dan tidak ada entri `System` baru

### Draft dan Borrowed tidak pernah ditutup otomatis
74. Verifikasi Draft `Alat Ukur Jarak Bosch {runId}` dan Draft `Meja Kerja Lipat {runId}` tetap `Draft` walau melewati batas Transaction timeout, karena Draft tidak memiliki timeout
75. Verifikasi baris `Pompa Air Honda {runId}`, `Vibrator Beton Wacker {runId}`, `Mixer Beton Molen {runId}`, dan `Penggetar Beton Bosch {runId}` tetap `Borrowed` dan tidak ditutup otomatis karena Transaction timeout hanya berlaku untuk status menunggu

### Draft hasil timeout bisa diajukan ulang
76. Principal mengubah status entitas menjadi `Active`
77. Hana mengajukan ulang Draft baris `Genset Yanmar 10kVA {runId}` untuk Borrower `Dedi Kurniawan {runId}`
78. Verifikasi Draft yang kembali dari timeout bisa diajukan ulang dan berstatus `Waiting for Approval`
79. Hana membatalkan pengajuan ulang baris `Genset Yanmar 10kVA {runId}`

### Draft hanya batal bila Borrower dinonaktifkan atau dibuang manual
80. Rina menonaktifkan Employee `Kirana Larasati {runId}`
81. Verifikasi Draft `Meja Kerja Lipat {runId}` batal karena Borrower dinonaktifkan, bukan karena timeout, sedangkan Draft `Alat Ukur Jarak Bosch {runId}` tetap `Draft`
82. Hana membuang Draft `Alat Ukur Jarak Bosch {runId}` secara manual lewat `Delete` di tab Drafts
83. Verifikasi Draft `Alat Ukur Jarak Bosch {runId}` hilang dari daftar Draft hanya karena dibuang manual, bukan ditutup otomatis

### Timeout Borrow pada level Basic membatalkan baris tanpa Draft baru
84. Principal mengubah level Feature Suite Borrowing plan entitas menjadi `Basic`
85. Hana mengajukan Borrow aset `Bor Beton Hilti {runId}` untuk Borrower `Eka Putri {runId}`
86. Hana mengajukan Borrow aset `Scaffolding Set Lengkap {runId}` untuk Borrower `Fitri Amelia {runId}`
87. Rudi menyetujui pengajuan Borrow aset `Scaffolding Set Lengkap {runId}`
88. Waktu berlalu sampai batas Transaction timeout `2` hari sejak masing-masing baris masuk statusnya terlewati
89. Job timeout transaksi berjalan
90. Verifikasi baris `Bor Beton Hilti {runId}` berstatus `Canceled` oleh `System` dan bukan Draft, dengan alasan `Timed out (Waiting for Approval)`
91. Verifikasi baris `Scaffolding Set Lengkap {runId}` berstatus `Canceled` oleh `System` dan bukan Draft, dengan alasan `Not picked up`
92. Verifikasi tidak ada Draft baru untuk baris `Bor Beton Hilti {runId}` maupun `Scaffolding Set Lengkap {runId}`
93. Verifikasi Custody aset `Bor Beton Hilti {runId}` dilepas dan status aset kembali `Available`
94. Verifikasi Custody aset `Scaffolding Set Lengkap {runId}` dilepas dan status aset kembali `Available`

### Toggle Approval Workflow OFF dan versi setting
95. Principal mematikan toggle Approval Workflow pada plan entitas
96. Verifikasi perubahan level plan dan toggle bukan perubahan Settings sehingga tidak masuk Changelog halaman Settings
97. Hana mengajukan Borrow aset `Mesin Gerinda Tangan Bosch {runId}` untuk Borrower `Gilang Ramadhan {runId}`
98. Verifikasi baris `Mesin Gerinda Tangan Bosch {runId}` langsung `Waiting for Handover` tanpa langkah approval dan Versi setting tercatat pada baris itu
99. Verifikasi Versi setting baris `Mesin Gerinda Tangan Bosch {runId}` sama dengan baris `Gerobak Dorong Besi {runId}` karena perubahan toggle dan level plan bukan perubahan Settings

### BRW asal dan Draft baru mencatat hasil timeout
100. Verifikasi BRW asal baris `Gerobak Dorong Besi {runId}` berstatus `Canceled` karena semua barisnya sudah tertutup
101. Verifikasi Draft baru tanpa nomor BRW dari baris `Gerobak Dorong Besi {runId}` memuat `Restored from [BRW no.]` dengan [BRW no.] nomor BRW asal baris itu
