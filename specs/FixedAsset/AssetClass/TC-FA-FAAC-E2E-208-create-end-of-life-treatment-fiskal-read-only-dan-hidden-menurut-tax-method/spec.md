---
id: TC-FA-FAAC-E2E-208-create-end-of-life-treatment-fiskal-read-only-dan-hidden-menurut-tax-method
title: "Create Asset Class: End-of-Life Treatment Fiskal Tampil Read-Only pada Tax Method Declining Balance dan Hidden pada Kondisi Lain"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-731
  - TC-FA-FAAC-732
sourceRules: ["FLD-34", "FAAC-LOGIC-02k", "FAAC-LOGIC-02g", "ST-36", "FI-18"]
smoke: []
dependsOn: []
trace:
  "FLD-34": [8, 9, 15, 19, 23]
  "FAAC-LOGIC-02k": [4, 6, 8, 15, 19, 23]
  "FAAC-LOGIC-02g": [18, 22]
  "ST-36": [4, 6, 8, 15, 19, 23]
  "FI-18": [8, 11, 12, 15, 19, 23]
coverage:
  web: automated
---

# Create Asset Class: End-of-Life Treatment Fiskal Tampil Read-Only pada Tax Method Declining Balance dan Hidden pada Kondisi Lain

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Tax Depreciation Class Active `Bukan bangunan – Kelompok 3` (metode yang diizinkan `Straight Line` dan `Declining Balance`; End-of-Life Treatment fiskal terisi pada master Tax Depreciation Class; nilainya tidak disebut TC, sehingga asersi langkah 9 membandingkan dengan nilai master yang dibaca dari `Fixture.fixed-asset-asset-class.<kunci>`), `Bangunan permanen` (hanya `Straight Line`), dan `Tanah` (tanpa metode). Ketiganya tanpa versi Scheduled pada keadaan awal spec ini. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE.
- Data Dinamis: tidak ada. Spec hanya mengisi Tax Depreciation Class dan Tax Method di form Create tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan nilai End-of-Life Treatment fiskal pada master Tax Depreciation Class `Bukan bangunan – Kelompok 3`; mencoba mengetik pada elemen read-only (langkah 10).
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-731: End-of-Life Treatment fiskal tampil read-only bila Tax Method Declining Balance

3. Verifikasi kartu Fiscal tampil
4. Verifikasi field End-of-Life Treatment fiskal tidak tampil
5. Pilih Tax Depreciation Class `Bukan bangunan – Kelompok 3`
6. Verifikasi field End-of-Life Treatment fiskal tidak tampil
7. Pilih Tax Method `Declining Balance`
8. Verifikasi field End-of-Life Treatment fiskal tampil sebagai teks read-only di samping Useful Life & Rate
9. Verifikasi nilai End-of-Life Treatment fiskal sama dengan data master Tax Depreciation Class `Bukan bangunan – Kelompok 3` (tanpa pola teks khusus)
10. Coba klik dan ketik pada field End-of-Life Treatment fiskal
11. Verifikasi field tidak dapat diubah
12. Verifikasi field bukan select maupun input

### TC-FA-FAAC-732: End-of-Life Treatment fiskal Hidden bila Tax Method bukan Declining Balance atau class tanpa metode

13. Ganti Tax Method menjadi `Straight Line`
14. Verifikasi kartu Fiscal tampil dengan Tax Method `Straight Line`
15. Verifikasi field End-of-Life Treatment fiskal tidak tampil
16. Pilih Tax Depreciation Class `Bangunan permanen`
17. Buka select Tax Method
18. Verifikasi select Tax Method hanya menawarkan `Straight Line`
19. Verifikasi field End-of-Life Treatment fiskal tidak tampil
20. Tutup select Tax Method tanpa mengubah pilihan
21. Pilih Tax Depreciation Class `Tanah`
22. Verifikasi Tax Method read-only `—`
23. Verifikasi field End-of-Life Treatment fiskal tidak tampil
24. Klik breadcrumb `Asset Class`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-731, TC-FA-FAAC-732). Tidak ada TC hanya-BE di spec ini. Aturan FATDC-LOGIC-03g (modul Tax Depreciation Class) disebut TC-731 sebagai sumber master dan tidak dimasukkan ke `sourceRules`.
- Satu pembukaan form dipakai bersama untuk kedua TC (prinsip 6 dan 8): langkah TC-732 "pilih Kelompok 3 dan Declining Balance lalu perhatikan End-of-Life Treatment fiskal" (Expected butir a: tampil read-only) menghasilkan keadaan yang sama dengan langkah 5 sampai 7, sehingga asersi langkah 8 dipakai untuk kedua TC dan tidak diulang. Langkah TC-732 selanjutnya dilanjutkan dari keadaan itu.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 20 (menutup select tanpa mengubah pilihan) dan langkah 24 sampai 26 (menutup form dirty, S-08). Langkah 3 dan 14 adalah anchor positif asersi absence (bagian 8b butir 2): kartu Fiscal sudah termuat sebelum field End-of-Life Treatment fiskal diasersi tidak tampil; keduanya tidak ada di Expected TC dan ditambahkan hanya sebagai anchor (S-03).
- Langkah 18 menjadi anchor positif bagi asersi absence langkah 19; langkah 22 menjadi anchor bagi langkah 23.
- Temuan untuk QA: (a) TC-731 langkah 5 ("coba klik dan ketik") tidak menyebut teks yang diketik; spec menulis langkah apa adanya dan mengasersi field tidak dapat diubah. (b) Nilai End-of-Life Treatment fiskal pada master `Bukan bangunan – Kelompok 3` tidak disebut TC; spec membandingkan dengan nilai master dari fixture. (c) Expected TC-732 butir c menyebut Tax Method "hanya menawarkan Straight Line"; spec mengasersi opsi tersebut pada langkah 18.
