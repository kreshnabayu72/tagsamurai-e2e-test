---
id: TC-FA-FAAC-E2E-041-create-validasi-input-digit-desimal
title: "Create Asset Class: Input Digit Desimal Ke-3 dan Pemisah Desimal Tidak Dapat Diketik"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-689
  - TC-FA-FAAC-690
  - TC-FA-FAAC-691
coverage:
  web: automated
---

# Create Asset Class: Input Digit Desimal Ke-3 dan Pemisah Desimal Tidak Dapat Diketik

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: tidak ada yang dipakai selain akun aktor. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec hanya mengetik di form Create tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: keystroke browser, termasuk menekan karakter `.` dan `,` pada field angka.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-689: Digit desimal ke-3 pada Declining Rate dan Residual Value berunit Percent

3. Pilih Method `Declining Balance`
4. Ketik Declining Rate `25.678`
5. Verifikasi Declining Rate menampilkan `25.67` (digit desimal ke-3 tidak dapat diketik)
6. Verifikasi nilai Declining Rate tidak dibulatkan menjadi `25.68`
7. Pada Residual Value pilih unit Percent
8. Ketik Residual Value `33.339`
9. Verifikasi Residual Value menampilkan `33.33` (digit desimal ke-3 tidak dapat diketik)
10. Verifikasi nilai Residual Value tidak dibulatkan menjadi `33.34`

### TC-FA-FAAC-690: Digit desimal ke-3 pada Residual Value berunit Amount dan Capitalization Threshold

11. Pada Residual Value pilih unit Amount dan kosongkan isinya
12. Ketik Residual Value `1500.999`
13. Verifikasi Residual Value menampilkan `1500.99` (boleh dengan pemisah ribuan; digit desimal ke-3 tidak dapat diketik)
14. Verifikasi nilai Residual Value tidak dibulatkan menjadi `1501.00`
15. Ketik Capitalization Threshold `2500000.999`
16. Verifikasi Capitalization Threshold menampilkan `2500000.99` (boleh dengan pemisah ribuan; digit desimal ke-3 tidak dapat diketik)
17. Verifikasi nilai Capitalization Threshold tidak dibulatkan menjadi `2500001.00`

### TC-FA-FAAC-691: Pemisah desimal tidak dapat diketik pada Useful Life dan Total Estimated Units

18. Pilih Method `Units of Production`
19. Ketik Useful Life `12`, lalu tekan karakter `.` dan karakter `,`
20. Verifikasi Useful Life tetap menampilkan `12`
21. Verifikasi karakter `.` dan `,` tidak muncul di field Useful Life (pecahan tidak dapat dimasukkan)
22. Ketik Total Estimated Units `500`, lalu tekan karakter `.` dan karakter `,`
23. Verifikasi Total Estimated Units tetap menampilkan `500`
24. Verifikasi karakter `.` dan `,` tidak muncul di field Total Estimated Units (pecahan tidak dapat dimasukkan)

### Penutup

25. Klik breadcrumb `Asset Class`
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-689 sampai 691). Tidak ada TC hanya-BE di spec ini. TC-FA-FAAC-700 dan TC-FA-FAAC-714 (tempel teks berpemisah desimal) ada di spec 042.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 1 dan tiap TC melanjutkan isian TC sebelumnya tanpa Submit.
- Langkah penghubung (S-03): langkah 2 (klik tab Depreciation sebelum memilih Method; TC-689 dan TC-690 tidak menyebut tab, TC-700 dan TC-714 menyebutnya), langkah 11 (mengganti unit Residual Value ke Amount dan mengosongkan isinya agar TC-690 tidak membawa nilai TC-689) dan langkah 25 sampai 27 (menutup form dirty, S-08).
- Klausa "nilai tidak dibulatkan menjadi X" pada Expected TC-689 dan TC-690 ditulis satu `Verifikasi` terpisah dari nilai yang tampil (langkah 6, 10, 14, 17), sesuai pemecahan klausa S-01.
- Temuan untuk QA:
  - TC-691 Expected a dan b menggabungkan "tetap menampilkan" dan "pemisah tidak muncul" yang teramati bersamaan; ditulis dua `Verifikasi` per field (nilai yang tampil; pemisah tidak muncul).
  - TC-690 tidak menyebut tab Capitalization Threshold berada; spec tidak menambah langkah pindah tab.
