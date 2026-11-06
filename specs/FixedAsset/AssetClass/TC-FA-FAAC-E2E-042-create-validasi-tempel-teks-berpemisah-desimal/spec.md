---
id: TC-FA-FAAC-E2E-042-create-validasi-tempel-teks-berpemisah-desimal
title: "Create Asset Class: Tempel Teks Berpemisah Desimal ke Useful Life, Total Estimated Units, dan Declining Rate"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-700
  - TC-FA-FAAC-714
coverage:
  web: automated
---

# Create Asset Class: Tempel Teks Berpemisah Desimal ke Useful Life, Total Estimated Units, dan Declining Rate

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: tidak ada yang dipakai selain akun aktor. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec hanya menempel teks di form Create tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: menempel (paste) teks dari clipboard browser ke field input.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-700: Teks berpemisah desimal yang ditempel ke Useful Life dan Total Estimated Units dipotong di pemisah pertama

3. Pilih Method `Units of Production`
4. Tempel (paste) teks `12.5` ke field Useful Life
5. Verifikasi Useful Life menampilkan `12` (tempelan dipotong di pemisah desimal pertama `.`, hanya bagian bilangan bulat yang masuk)
6. Verifikasi nilai Useful Life tidak menjadi `125` dan tempelan tidak ditolak seluruhnya (field tidak kosong)
7. Tempel (paste) teks `80,000` ke field Total Estimated Units
8. Verifikasi Total Estimated Units menampilkan `80` (tempelan dipotong di pemisah pertama `,`, hanya bagian bilangan bulat yang masuk)
9. Verifikasi nilai Total Estimated Units tidak menjadi `80000` dan tempelan tidak ditolak seluruhnya (field tidak kosong)
10. Verifikasi tidak ada caption error pada Useful Life dan Total Estimated Units

### TC-FA-FAAC-714: Teks berpemisah desimal yang ditempel ke Declining Rate diperlakukan seperti diketik

11. Pilih Method `Declining Balance`
12. Tempel (paste) teks `12.345` ke field Declining Rate
13. Verifikasi Declining Rate menampilkan `12.34` (pemisah desimal pertama diterima dan digit desimal ke-3 tidak masuk ke field)
14. Verifikasi nilai Declining Rate tidak dibulatkan menjadi `12.35` dan tempelan tidak ditolak seluruhnya
15. Verifikasi tidak ada caption error pada Declining Rate

### Penutup

16. Klik breadcrumb `Asset Class`
17. Verifikasi dialog `Unsaved Changes` tampil
18. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-700 dan TC-FA-FAAC-714). Tidak ada TC hanya-BE di spec ini.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 1 dan tab Depreciation dibuka pada langkah 2; TC-714 mengulang langkah pembuka TC itu (klik tab Depreciation, pilih Method) dari form yang sama.
- Langkah penghubung (S-03): langkah 16 sampai 18 (menutup form dirty, S-08). Langkah 2 mengklik tab Depreciation sesuai TC-700 dan TC-714.
- Asersi "tidak ada caption error" (langkah 10 dan 15) didahului `Verifikasi` nilai pada field yang sama (langkah 5, 8, 13) sebagai anchor positif.
- Temuan untuk QA:
  - TC-700 Expected a dan b menggabungkan "dipotong di pemisah pertama" dengan dua negasi ("tidak menjadi 125/80000" dan "tidak ditolak seluruhnya"); negasi ditulis satu `Verifikasi` per field (langkah 6 dan 9).
