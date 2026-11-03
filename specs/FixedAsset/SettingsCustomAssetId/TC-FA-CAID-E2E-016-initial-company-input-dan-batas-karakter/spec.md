---
id: TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter
title: "Initial Company: Checkbox, Kapital Otomatis, dan Batas 5 Karakter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-48
  - TC-FA-CAID-49
  - TC-FA-CAID-50
  - TC-FA-CAID-51
coverage:
  web: automated
---

# Initial Company: Checkbox, Kapital Otomatis, dan Batas 5 Karakter

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Spec hanya mengetik dan mengamati: tidak menekan `[Save]`, tidak membuat data, tidak mengubah state global. Satu pembukaan form dipakai untuk seluruh TC; input dikosongkan dan checkbox dihilangkan centangnya antar TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-48: Mencentang checkbox Initial Company meng-enable input

1. Verifikasi input Initial Company berstatus disabled
2. Centang checkbox `Initial Company`
3. Verifikasi input Initial Company berstatus enabled
4. Verifikasi placeholder `Enter initial company` tampil pada input Initial Company
5. Verifikasi Live Preview tetap `JKT/LAP/T490/0926/1` tanpa token Initial Company dan tanpa pemisah tambahan karena input masih kosong
6. Verifikasi tombol `[Save]` aktif
7. Hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-49: Meng-uncheck Initial Company men-disable input tanpa menghapus nilai

8. Centang checkbox `Initial Company` dan ketik `ABC` pada input Initial Company
9. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0926/1`
10. Hilangkan centang checkbox `Initial Company`
11. Verifikasi input Initial Company berstatus disabled
12. Verifikasi input Initial Company tetap berisi `ABC`
13. Verifikasi Live Preview kembali menampilkan `JKT/LAP/T490/0926/1`
14. Centang kembali checkbox `Initial Company`
15. Verifikasi input Initial Company berstatus enabled
16. Verifikasi input Initial Company berisi `ABC`
17. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0926/1` lagi
18. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-50: Huruf kecil menjadi kapital secara langsung

19. Centang checkbox `Initial Company`
20. Ketik huruf kecil `abc12` pada input Initial Company
21. Verifikasi input menampilkan `ABC12`
22. Verifikasi tidak ada pesan error pada input Initial Company
23. Verifikasi Live Preview menampilkan `ABC12/JKT/LAP/T490/0926/1`
24. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

### TC-FA-CAID-51: Karakter ke-6 tidak dimasukkan dan menampilkan Max. 5 characters

25. Centang checkbox `Initial Company`
26. Ketik `ABCDEF` satu per satu pada input Initial Company
27. Verifikasi input tetap berisi `ABCDE`
28. Verifikasi pesan `Max. 5 characters` tampil di bawah input
29. Verifikasi helper text `Prefix identifier representing your company entity (up to 5 characters, letters and numbers only). Required when checked.` tidak tampil karena digantikan pesan
30. Tekan Backspace sekali, lalu ketik `Z`
31. Verifikasi input berisi `ABCDZ`
32. Verifikasi pesan `Max. 5 characters` tidak tampil
33. Verifikasi helper text `Prefix identifier representing your company entity (up to 5 characters, letters and numbers only). Required when checked.` tampil lagi
34. Verifikasi tombol `[Save]` aktif dan tidak diblokir oleh pesan ini
35. Kosongkan input Initial Company, lalu hilangkan centang checkbox `Initial Company`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 7, 18, 24, dan 35 (mengosongkan input dan menghilangkan centang antar TC, S-09). Langkah 35 sekaligus memulihkan form yang berakhir dirty; form tidak disimpan sehingga tidak ada state tersimpan yang berubah.
- Langkah 1 adalah keadaan awal field sebelum dicentang (Expected TC-FA-CAID-48 a menyebut perubahan dari disabled ke enabled).
- Absence pada langkah 22 dan 32 memakai nilai input (langkah 21 dan 31) sebagai anchor positif pada surface yang sama. Langkah 29 memakai pesan pada langkah 28 sebagai anchor.
- Spec ini 35 langkah; tidak ada langkah yang diulang selain pola centang dan kosongkan antar TC.
- Temuan untuk QA:
  - Expected TC-FA-CAID-48 c ("Tombol `[Save]` berubah menjadi aktif") tidak menyebut apakah input masih kosong memenuhi validasi; spec hanya mengasersi `[Save]` aktif, sesuai TC (validasi kosong diuji TC-FA-CAID-57 di spec 018).
  - Expected TC-FA-CAID-51 c ("tidak diblokir oleh pesan ini") ditulis sebagai `[Save]` aktif karena TC tidak memberi langkah menekan `[Save]`.
