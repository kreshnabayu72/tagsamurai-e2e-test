---
id: TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus
title: "Search Tabel Asset Class: Accounts, Modified By, Nama Asset Name, dan Kolom yang Tidak Dicari"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-355
  - TC-FA-FAAC-356
  - TC-FA-FAAC-357
  - TC-FA-FAAC-358
  - TC-FA-FAAC-359
sourceRules: ["§5#b2", "§4.1.1#r7", "§4.1.1#b1", "§4.1#r10", "§4.4#r15", "§4.1.1#r10", "§4.1.1#r11"]
smoke: []
dependsOn: []
trace:
  "§5#b2": [2, 3, 4, 7, 10, 11, 29]
  "§4.1.1#r7": [2, 3, 4, 7, 10]
  "§4.1.1#b1": [14, 16]
  "§4.1#r10": 20
  "§4.4#r15": 20
  "§4.1.1#r10": [20, 23]
  "§4.1.1#r11": 29
coverage:
  web: automated
---

# Search Tabel Asset Class: Accounts, Modified By, Nama Asset Name, dan Kolom yang Tidak Dicari

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Kondisi Accounts: IT-EQ memiliki satu akun Inactive berkode 1520 (tooltip `Account 1520 is inactive. Journals for this asset class will be held at export.`), MACHINERY dan LAND belum lengkap, enam kelas lain lengkap. OFFICE-OLD berstatus Inactive dengan Accounts lengkap. Modified By (aktor entri Changelog terbaru): HEAVY-EQ, VEHICLES, MACHINERY, dan OFFICE-NEW = Rina P; OFFICE-OLD = Budi S; IT-EQ dan STORAGE = System (entri terbaru dari job); BLDG dan LAND = System (belum ada entri Changelog). Asset Name Excavator PC200 dan Wheel Loader ter-assign ke HEAVY-EQ; Asset Name Delivery Van ter-assign ke VEHICLES. Seed disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: konfigurasi kolom tabel (kolom Modified By dan Last Updated ditampilkan oleh spec ini). Dipulihkan oleh langkah 31 dan oleh hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data Asset Class.

## Test Steps

### TC-FA-FAAC-355: Search pada kolom Accounts mencocokkan teks kondisi

1. Ketik Search `Complete`, tekan Enter, lalu telusuri seluruh halaman hasil dari halaman 1 sampai halaman terakhir (Next)
2. Verifikasi baris berkondisi lengkap tampil: BLDG, HEAVY-EQ, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES
3. Verifikasi baris berkondisi belum lengkap (LAND, MACHINERY) juga tampil karena teks incomplete memuat complete
4. Verifikasi baris IT-EQ tidak tampil
5. Klik `✕` pada Search, tekan Enter
6. Ketik Search `incomplete`, tekan Enter
7. Verifikasi hanya baris LAND dan MACHINERY yang tampil: kedua baris tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
8. Klik `✕` pada Search, tekan Enter
9. Ketik Search `inactive`, tekan Enter
10. Verifikasi hanya baris IT-EQ yang tampil (cocok dengan teks tooltip `Account 1520 is inactive. Journals for this asset class will be held at export.`): baris IT-EQ tampil dan baris contoh lain (HEAVY-EQ) tidak tampil

### TC-FA-FAAC-358: Search tidak mencocokkan toggle kolom Active

11. Verifikasi baris OFFICE-OLD (status Inactive pada toggle) tidak tampil pada hasil Search `inactive` langkah 9 karena toggle Active tidak ikut dicari

### TC-FA-FAAC-357: Search juga mencocokkan nama Asset Name di dalam Asset Class

12. Klik `✕` pada Search, tekan Enter
13. Ketik Search `excavator`, tekan Enter
14. Verifikasi baris HEAVY-EQ tampil meskipun kata itu tidak ada di kolom lain
15. Ganti isi kotak search dengan `DELIVERY VAN`, tekan Enter
16. Verifikasi baris VEHICLES tampil

### TC-FA-FAAC-356: Search pada kolom Modified By yang ditampilkan lewat Setup Column

17. Klik `✕` pada Search, tekan Enter
18. Aktifkan kolom Modified By lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Modified By), klik `[Save]`
19. Ketik Search `rina`, tekan Enter, lalu telusuri seluruh halaman hasil dari halaman 1 sampai halaman terakhir (Next)
20. Verifikasi baris HEAVY-EQ, MACHINERY, OFFICE-NEW, dan VEHICLES tampil
21. Klik `✕` pada Search, tekan Enter
22. Ketik Search `system`, tekan Enter, lalu telusuri seluruh halaman hasil dari halaman 1 sampai halaman terakhir (Next)
23. Verifikasi baris BLDG, IT-EQ, LAND, dan STORAGE tampil

### TC-FA-FAAC-359: Search tidak mencocokkan teks tanggal kolom Last Updated

24. Klik `✕` pada Search, tekan Enter
25. Aktifkan kolom Last Updated lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Last Updated), klik `[Save]`
26. Ketik Search `HEAVY-EQ`, tekan Enter
27. Salin teks tanggal (tanpa jam) pada kolom Last Updated baris HEAVY-EQ
28. Ganti isi kotak Search dengan tempel teks tanggal itu, tekan Enter
29. Verifikasi empty state `No results found` tampil karena kolom tanggal tidak dicari; penyaringan tanggal hanya lewat Filter Panel
30. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
31. Sembunyikan kembali kolom Modified By dan Last Updated lewat Setup Column (hilangkan centang keduanya), klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 5, 8, 12, 17, 21, 24 (mengosongkan kotak Search antar kata kunci, S-09; 8b butir 9), langkah 26 (Search `HEAVY-EQ` untuk menemukan baris target sebelum menyalin tanggal, R-16; TC-359 Data d), langkah 27 (menyalin teks tanggal sebagai bahan Search; TC langkah 3), langkah 30 (menutup input Search dan mereset tabel, S-09; R-16), langkah 31 (memulihkan konfigurasi kolom, S-09).
- Urutan TC di dalam spec: TC-FA-FAAC-358 diletakkan tepat setelah TC-FA-FAAC-355 karena memakai kata kunci `inactive` yang sama; langkah 11 hanya mengamati hasil Search langkah 9 (anchor positif baris IT-EQ pada `Verifikasi` langkah 10 membuktikan tabel termuat, 8b butir 2). Kolom Modified By dan Last Updated diaktifkan di akhir (TC-FA-FAAC-356 dan 359) supaya blok Search tidak bergantung pada konfigurasi kolom.
- Penelusuran seluruh halaman pada langkah 1, 19, dan 22 (S-14) menjadi bagian langkah Search karena hasil `Complete`, `rina`, dan `system` mencakup seed lain dan dapat melampaui satu halaman; asersi hanya pada keanggotaan baris contoh.
- Klausa "hanya baris tersebut yang tampil" diasersi sebagai satu `Verifikasi` per kata kunci dengan satu baris pembanding yang dijamin ada.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kondisi persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
