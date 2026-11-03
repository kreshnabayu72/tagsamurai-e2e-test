---
id: TC-FA-CAT-E2E-152-gerbang-warranty-dan-custom-field-purchasing-purchase-group-a
title: "Gerbang Warranty dan Custom Field Purchasing untuk Purchase Group A: Group A Saja, Search Tidak Mencocokkan No access, dan Keadaan Tidak Berlaku Menang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-671
  - TC-FA-CAT-676
  - TC-FA-CAT-686
coverage:
  web: automated
---

# Gerbang Warranty dan Custom Field Purchasing untuk Purchase Group A: Group A Saja, Search Tidak Mencocokkan No access, dan Keadaan Tidak Berlaku Menang

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Purchase Group A (Pre-setup #53) `purchaseGroupA_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role Manage purchase hanya pada group `Head Office` beserta descendant; tanpa View asset value dan Manage accounting), client CatMain (Pre-setup #20), password `Spectra.env.FA_PGA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun Ganti akun (TC-FA-CAT-676): Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FS_PASSWORD`.
- Env var `FA_PGA_PASSWORD` dan `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 dan #56 (CatMain, node `Laptop`, seed API; lisensi FA-7 aktif): Warranty Expiry `Laptop Dell - 1` 2027-03-15, `Laptop Dell - 2` tanpa nilai, `Laptop HP - 3` 2027-06-30 (di luar group A); Asset Value `Laptop Dell - 1` 15000000.00; Custom Field Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell` (Text, Scope Specific Asset Name `Laptop Dell`; `Laptop Dell - 1` `KD-01`), `Nomor PO` (Text, Scope General; `Laptop Dell - 1` `PO-0001`, `Laptop HP - 3` `PO-0099`, `Laptop Dell - 3` tanpa nilai); Accounting `Kode Anggaran`. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-671: Gerbang Warranty dan Custom Field Purchasing untuk pemegang Manage purchase pada group A

3. Klik header Actions (⋯) > `Setup Column...`
4. Verifikasi daftar kolom Custom Field memuat kolom Purchasing (`Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`)
5. Verifikasi daftar kolom Custom Field tidak memuat `Kode Anggaran` (Accounting)
6. Centang `Asset Value`, `Warranty Expiry`, dan `Nomor PO`, lalu klik `[Save]`
7. Verifikasi sel Warranty Expiry `Laptop Dell - 1` menampilkan nilainya
8. Verifikasi sel Warranty Expiry `Laptop Dell - 2` menampilkan `—`
9. Verifikasi sel `Nomor PO` `Laptop Dell - 1` menampilkan `PO-0001`
10. Verifikasi sel `Nomor PO` `Laptop Dell - 3` menampilkan `—`
11. Klik kontrol halaman berikutnya
12. Verifikasi sel Warranty Expiry `Laptop HP - 3` menampilkan `No access`
13. Verifikasi sel `Nomor PO` `Laptop HP - 3` menampilkan `No access`
14. Hover sel `No access` pada `Nomor PO` `Laptop HP - 3`
15. Verifikasi hover menampilkan `Requires Manage purchase access in this group.`
16. Klik kontrol halaman sebelumnya
17. Verifikasi seluruh sel Asset Value menampilkan `No access` (Manage purchase bukan hak Asset Value)
18. Hover salah satu sel Asset Value
19. Verifikasi hover menampilkan `Requires View asset value access in this group.`

### TC-FA-CAT-686: Keadaan tidak berlaku menang atas No access

20. Buka Setup Column, centang `Nomor Kontrak Dell` (kolom `Nomor PO` sudah tercentang), lalu klik `[Save]`
21. Verifikasi sel `Nomor Kontrak Dell` `Laptop Dell - 1` menampilkan `KD-01`
22. Verifikasi sel `Nomor Kontrak Dell` `Laptop Dell - 3` menampilkan `—` (berhak, nilai belum ada)
23. Klik kontrol halaman berikutnya
24. Verifikasi sel `Nomor Kontrak Dell` `Laptop HP - 3` menampilkan `—` karena field tidak berlaku bagi Asset Name `Laptop HP`, bukan `No access` dan tanpa hover `No access`
25. Verifikasi sel `Nomor PO` `Laptop HP - 3` menampilkan `No access` karena field berlaku dan aktor tidak berhak atas baris itu
26. Klik kontrol halaman sebelumnya

### TC-FA-CAT-676: Search tidak mencocokkan nilai maupun teks No access

27. Ketik Search `PO-0099`, tekan Enter
28. Verifikasi `No results found` dengan `Try adjusting your search or filter.` tampil dan `Laptop HP - 3` tidak ditemukan
29. Klik `(←)` pada kotak Search
30. Ketik Search `No access`, tekan Enter
31. Verifikasi tidak ada baris yang ditemukan
32. Klik `(←)` pada kotak Search
33. Ketik Search `15.000.000`, tekan Enter
34. Verifikasi tidak ada baris yang ditemukan karena sel Asset Value `No access` tidak cocok dengan nilai
35. Klik `(←)` pada kotak Search
36. Ganti akun: login sebagai Full Sensitive, pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
37. Buka Setup Column, centang `Nomor PO` dan `Asset Value`, lalu klik `[Save]`
38. Ketik Search `PO-0099`, tekan Enter
39. Verifikasi `Laptop HP - 3` ditemukan
40. Ganti isi kotak search dengan `15.000.000`, tekan Enter
41. Verifikasi `Laptop Dell - 1` ditemukan

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 41). Alasan: tiga TC memakai Popup Detail `Laptop` dan kolom yang disiapkan sekali; ekspansi berasal dari butir Expected bermajemuk yang dipecah per klausa (S-01) dan satu pergantian akun.
- Urutan blok: TC-FA-CAT-686 didahulukan sebelum TC-FA-CAT-676 karena TC-FA-CAT-676 berakhir di akun lain (S-10).
- Langkah penghubung (S-03, S-07, S-09): langkah 1 dan 2 (membuka Popup Detail), pindah halaman 2 dan kembali (S-14), `(←)` pada Search, dan Ganti akun ke Full Sensitive.
- Pemetaan plan: baris plan menyebut tier Group Manager (#9), tetapi ketiga TC sumber tidak memakainya; GM tidak dimasukkan.
- Temuan untuk QA:
  - TC-FA-CAT-676 langkah 5 mencentang `Asset Value` pada tabel dan Search `15.000.000`; format sel `15.000.000` untuk Full Sensitive bergantung format tampilan sel (Rp), sehingga hanya ditemukan bila potongan itu cocok.
  - TC-FA-CAT-671 langkah 6 menyebut hover sel `Asset Value` pada "salah satu" baris; spec meng-hover satu sel.
  - TC-FA-CAT-671 Expected b menyebut tanggal tanpa memberi format; spec mengasersi nilainya tampil.
  - Nama env var `FA_PGA_PASSWORD` dan `FA_FS_PASSWORD` adalah usulan; TC tidak menyebut nama env var.
