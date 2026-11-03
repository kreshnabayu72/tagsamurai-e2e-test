---
id: TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview
title: "Initial Company: Paste, Karakter Terlarang, dan Live Preview Kosong"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-52
  - TC-FA-CAID-53
  - TC-FA-CAID-54
  - TC-FA-CAID-58
coverage:
  web: automated
---

# Initial Company: Paste, Karakter Terlarang, dan Live Preview Kosong

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): paste teks dari clipboard ke input (langkah 2 dan 20).
- Spec hanya mengetik dan mengamati: tidak menekan `[Save]`, tidak membuat data, tidak mengubah state global. Satu pembukaan form dipakai untuk seluruh TC; input dikosongkan dan checkbox dihilangkan centangnya antar TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-52: Paste lebih dari 5 karakter dipotong ke 5 karakter

1. Centang checkbox `Initial Company`
2. Paste teks `ABCDEFGH` ke input Initial Company
3. Verifikasi input berisi `ABCDE`
4. Verifikasi pesan `Max. 5 characters` tampil di bawah input
5. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-53: Karakter di luar A-Z dan 0-9 tidak dimasukkan saat diketik

6. Centang checkbox `Initial Company`
7. Ketik `A`, `B`, lalu `-` pada input Initial Company
8. Verifikasi karakter `-` tidak masuk ke input dan input tetap berisi `AB`
9. Verifikasi pesan `Initial company contains invalid characters` tampil di bawah input
10. Verifikasi helper text `Prefix identifier representing your company entity (up to 5 characters, letters and numbers only). Required when checked.` tidak tampil karena digantikan pesan
11. Ketik `C` pada input Initial Company
12. Verifikasi input berisi `ABC`
13. Verifikasi pesan `Initial company contains invalid characters` tidak tampil
14. Ketik `D` pada input Initial Company
15. Verifikasi input berisi `ABCD`
16. Verifikasi helper text `Prefix identifier representing your company entity (up to 5 characters, letters and numbers only). Required when checked.` tampil lagi
17. Verifikasi tombol `[Save]` aktif dan tidak diblokir oleh pesan ini
18. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-54: Paste teks berkarakter terlarang disaring dan diubah ke kapital

19. Centang checkbox `Initial Company`
20. Paste teks `a b!c#1` ke input Initial Company
21. Verifikasi input berisi `ABC1`
22. Verifikasi pesan `Initial company contains invalid characters` tampil di bawah input
23. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-58: Initial Company dicentang tetapi kosong tidak menampilkan token maupun pemisah

24. Centang checkbox `Initial Company`
25. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1` tanpa token kosong dan tanpa pemisah di awal
26. Ketik `ABC` pada input Initial Company
27. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0926/1`
28. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5, 18, 23, dan 28 (mengosongkan input dan menghilangkan centang antar TC; langkah 18 juga memisahkan pesan `Initial company contains invalid characters` TC-FA-CAID-53 dari TC-FA-CAID-54, R-12). Langkah 28 memulihkan form yang berakhir dirty; form tidak pernah disimpan.
- Absence pada langkah 13 memakai input langkah 12 sebagai anchor positif pada surface yang sama.
- Temuan untuk QA:
  - TC-FA-CAID-52 b menyebut pesan `Max. 5 characters` setelah paste 8 karakter; TC tidak menyatakan apakah pesan itu hilang dengan sendirinya. Spec tidak mengasersi keadaan pesan setelah langkah 4.
  - TC-FA-CAID-53 c ("tidak diblokir oleh pesan ini") ditulis sebagai `[Save]` aktif karena TC tidak memberi langkah menekan `[Save]`.
  - Kemampuan paste clipboard tidak tertulis di TC; dicatat sebagai kebutuhan tim FE di Prerequisites.
