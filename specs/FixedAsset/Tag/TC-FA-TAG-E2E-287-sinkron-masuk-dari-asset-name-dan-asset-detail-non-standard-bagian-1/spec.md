---
id: TC-FA-TAG-E2E-287-sinkron-masuk-dari-asset-name-dan-asset-detail-non-standard-bagian-1
title: "Sinkron Masuk dari Asset Name dan Asset Detail: Non-standard Mengikuti TAG Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1133
  - TC-FA-TAG-1134
  - TC-FA-TAG-1139
  - TC-FA-TAG-1140
  - TC-FA-TAG-1141
  - TC-FA-TAG-1142
coverage:
  web: automated
---

# Sinkron Masuk dari Asset Name dan Asset Detail: Non-standard Mengikuti TAG Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): grup Excavator 20 Ton / Plant A (20 aset: 18 ber-Tag RFID dan 2 Not Paired Yet; TAG Type Asset Name RFID) dan Excavator 20 Ton / Plant B (20 aset); pemegang Update Plant A: Budi S.
- Baseline nilai kartu `Non-standard` dan Non-standard baris Excavator 20 Ton / Plant A dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` (S-12).
- Perubahan TAG Type Asset Name dipicu lewat sesi API karena objek uji ada di halaman TAG; hasilnya diamati di sesi UI akun aktor (kemampuan disediakan tim BE/FE).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: TAG Type Asset Name 'Excavator 20 Ton' (dan Asset Name lain yang disebut pada langkah). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1133: ubah TAG Type dari RFID ke NFC membuat Tag RFID Non-standard

1. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC hingga perubahan tersimpan
2. Muat ulang halaman TAG tab Paired (F5)
3. Verifikasi Non-standard baris Excavator 20 Ton / Plant A dihitung ulang menjadi 18 (aset ber-Tag RFID)
4. Verifikasi kartu `Non-standard` bertambah 18 terhadap nilai sebelum perubahan
5. Verifikasi kolom TAG Type baris Excavator 20 Ton / Plant A menampilkan NFC
6. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
7. Arahkan kursor ke ikon peringatan di samping salah satu Tag RFID
8. Verifikasi setiap Tag RFID di Popup Detail memiliki ikon peringatan dengan tooltip `This TAG type is not required by the asset name.`

### TC-FA-TAG-1134: mengembalikan TAG Type ke RFID mengurangi Non-standard

9. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari NFC menjadi RFID hingga perubahan tersimpan
10. Muat ulang halaman TAG tab Paired (F5)
11. Verifikasi Non-standard baris Excavator 20 Ton / Plant A kembali 0 tanpa tindakan Replace
12. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Verifikasi ikon peringatan hilang dari Tag RFID di Popup Detail

### TC-FA-TAG-1139: menambah tipe pada Asset Name tidak membuat Tag yang ada Non-standard

14. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi RFID dan NFC hingga perubahan tersimpan
15. Muat ulang halaman TAG tab Paired (F5)
16. Verifikasi Non-standard baris Excavator 20 Ton / Plant A tetap 0
17. Verifikasi aset ber-Tag RFID tidak terhitung Non-standard
18. Verifikasi aset ber-Tag RFID tidak menjadi Not Paired Yet

### TC-FA-TAG-1140: Asset Name diubah menjadi Non-TAG

19. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' menjadi Non TAG hingga perubahan tersimpan
20. Muat ulang halaman TAG tab Paired (F5)
21. Verifikasi kolom TAG Type baris Excavator 20 Ton / Plant A menampilkan badge `Non TAG`
22. Verifikasi Non-standard baris Excavator 20 Ton / Plant A = 18
23. Verifikasi baris grup Excavator 20 Ton / Plant A tetap tampil di tab Paired

### TC-FA-TAG-1141: Non-standard diperbarui pada setiap pemuatan data tanpa penyimpanan flag

24. Pulihkan TAG Type 'Excavator 20 Ton' ke RFID lewat fixture backend, muat ulang halaman, lalu catat Non-standard baris Plant A (0)
25. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC hingga perubahan tersimpan
26. Tekan F5 pada tab Paired
27. Verifikasi nilai Non-standard baris Plant A mengikuti TAG Type terbaru (18) setelah F5
28. Verifikasi tidak ada kontrol sinkronisasi manual pada halaman TAG

### TC-FA-TAG-1142: aset Not Paired Yet pada Popup Detail selaras dengan dimensi Tagging di Asset Detail

29. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
30. Klik `Show` di samping `Not Paired Yet`, lalu catat satu aset berstatus `Not Paired Yet`
31. Buka Asset > Asset List > Detail aset yang dicatat
32. Verifikasi Asset Detail aset itu menampilkan status Tagging `Not Paired Yet`
33. Verifikasi aset itu tidak memiliki Tag Paired

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 24 (memulihkan TAG Type dan mencatat nilai awal).
- TC-FA-TAG-1143 ada di spec 288. TC-FA-TAG-1134 melanjutkan keadaan TC-FA-TAG-1133 (TAG Type NFC), sesuai dependensinya.
- Urutan: TC-FA-TAG-1139 dan 1140 menetapkan TAG Type secara absolut sehingga tidak butuh pemulihan antar keduanya; pemulihan ke RFID hanya sebelum TC-FA-TAG-1141 yang mensyaratkan Non-standard awal 0.
- Temuan untuk QA:
  - TC-FA-TAG-1133 langkah TC ke-1 dan TC-FA-TAG-1134 langkah TC ke-1 mengubah TAG Type lewat Modul Asset Name; spec memicunya lewat sesi API dan tidak menguji form Asset Name (bukan objek uji).
  - TC-FA-TAG-1141 langkah TC ke-2 ('Ubah TAG Type pada Asset Name') tidak menyebut Asset Name dan nilai; spec memakai 'Excavator 20 Ton' dari RFID menjadi NFC seperti TC-FA-TAG-1133.
  - TC-FA-TAG-1141 Expected b ('Tidak ada sinkronisasi manual') tidak punya langkah observasi; spec mengasersi tidak ada kontrol sinkronisasi manual di halaman TAG.
  - TC-FA-TAG-1142 langkah TC ke-2 ('Catat satu aset dengan Status Not Paired Yet') tidak menyebut cara menampilkannya; spec memakai `Show` di samping `Not Paired Yet`.
  - TC-FA-TAG-1133 sampai 1142 Post Condition (mis. 'Tidak ada objek tugas atau dokumen yang dibuat', 'Notifikasi in-app tercatat') tanpa langkah observasi tidak diasersi.
