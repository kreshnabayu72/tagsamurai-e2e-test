---
id: TC-AC-PF-E2E-167-setup-column-tab-assigned-clients-geser-pin-reset
title: "Setup Column Tab Assigned Clients: geser urutan, Pin dan Unpin, dan Reset to Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-432
  - TC-AC-PF-433
  - TC-AC-PF-434
coverage:
  web: automated
---

# Setup Column Tab Assigned Clients: geser urutan, Pin dan Unpin, dan Reset to Default

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE); pengaturan lebar viewport browser. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec menyimpan konfigurasi kolom Tab Assigned Clients (urutan, Pin) dan mengubah lebar viewport; langkah 34 dan hook `after` menghapus preferensi kolom dan memulihkan viewport. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Geser urutan kolom (TC-AC-PF-432)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Buka Popup Setup Column (klik header kolom Actions (`⋯`), lalu `Setup Column...`).
4. Drag kolom `Plan Version` ke posisi paling awal.
5. Verifikasi Live Preview menampilkan `Plan Version` di posisi pertama sebelum Save.
6. Klik `[Save]`.
7. Tekan F5.
8. Verifikasi urutan header tabel dimulai dari `Plan Version`.

### Reset to Default (TC-AC-PF-434)

9. Buka Popup Setup Column.
10. Uncheck kolom `Assigned By`.
11. Drag kolom `Plan Version` ke posisi awal.
12. Klik `[Save]`.
13. Buka Popup Setup Column lagi.
14. Klik `[Reset to Default]`.
15. Verifikasi Live Preview menampilkan kolom dengan urutan default `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By`.
16. Klik `[Save]`.
17. Verifikasi tabel kembali ke urutan dan visibilitas default (kolom `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By`).
18. Tekan F5.
19. Verifikasi tabel tetap berada pada urutan dan visibilitas default setelah F5.

### Pin dan Unpin kolom (TC-AC-PF-433)

20. Perkecil lebar viewport sehingga tabel dapat di-scroll horizontal.
21. Buka Popup Setup Column.
22. Klik icon Pin pada kolom `Client Name`.
23. Klik `[Save]`.
24. Scroll tabel ke kanan.
25. Verifikasi kolom `Client Name` tetap terlihat di sisi kiri saat tabel di-scroll horizontal (freeze).
26. Tekan F5.
27. Scroll tabel ke kanan.
28. Verifikasi kolom `Client Name` masih beku setelah F5.
29. Buka Popup Setup Column.
30. Klik icon Pin `Client Name` lagi (Unpin).
31. Klik `[Save]`.
32. Scroll tabel ke kanan.
33. Verifikasi kolom `Client Name` ikut bergeser saat tabel di-scroll horizontal.
34. Pulihkan viewport ke lebar semula dan hapus preferensi Setup Column Tab Assigned Clients di browser (kemampuan disediakan tim FE).

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 34 (memulihkan viewport dan konfigurasi kolom, bagian 4 konvensi).
- Urutan TC dalam spec: TC-AC-PF-434 ditulis sebelum TC-AC-PF-433 karena Reset to Default (langkah 14 sampai 19) mengembalikan urutan dan visibilitas kolom ke default sehingga TC-AC-PF-433 berjalan di atas konfigurasi default tanpa langkah pemulihan tambahan.
- Langkah 11 menggeser kolom `Plan Version` yang sudah berada di posisi pertama sejak langkah 4 sampai 7; langkah itu disalin dari TC-AC-PF-434 apa adanya.
- Langkah 4 sampai 7: Live Preview diasersi sebelum `[Save]` (bagian 8b butir 5).
- Temuan untuk QA:
  - Post Condition TC-AC-PF-432 ("Urutan kolom tersimpan di localStorage") dan TC-AC-PF-433 ("Status pin tersimpan di localStorage") tidak punya langkah observasi di TC; persistensi hanya teramati lewat F5 dan Post Condition tidak diasersi terpisah.
  - TC-AC-PF-433 tidak menyebut lebar viewport yang membuat tabel scroll horizontal; nilainya perlu ditetapkan tim FE.
  - TC-AC-PF-434 mengandalkan keadaan awal default Setup Column; pada rangkaian ini keadaan tersebut dipenuhi sesudah langkah 8 hanya lewat Reset to Default, sehingga langkah 9 sampai 12 mengubah konfigurasi yang sudah tersimpan dari TC-AC-PF-432.
