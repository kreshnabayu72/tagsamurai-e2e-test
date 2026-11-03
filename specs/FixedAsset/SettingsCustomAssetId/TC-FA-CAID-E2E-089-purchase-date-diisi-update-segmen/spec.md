---
id: TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen
title: "Purchase Date: Diisi Pertama Kali, Log Cascade, Idempotent, dan Diubah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-277
  - TC-FA-CAID-278
  - TC-FA-CAID-254
  - TC-FA-CAID-283
coverage:
  web: automated
---

# Purchase Date: Diisi Pertama Kali, Log Cascade, Idempotent, dan Diubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Targeted (Pre-setup No 29; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE; pengguna Sarah Johnson), password `Spectra.env.FA_TARGETED_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Targeted (No 29), hook `before` men-seed konfigurasi B3 (Slash; Group, Category, Asset Name, Division, Purchase Date, Increment) dan aset Draft D1 `JKT/LAP/T490/0000/0000/1` (Purchase Date dan Division kosong), D2, D3 Draft `JKT/LAP/T490/HR/0926/3`, D4 Active, D5 Waiting for Approval; General Settings Date Format `dd/MM/yy`, Time Format 24 jam (No 27). Purchase Date, Purchase Price `15000000`, dan faktur `invoice.pdf` (berkas dari fixture, belum ada; prasyarat tahap script yang disediakan tim FE/BE) sesuai Data Uji.
- Data Dinamis: Purchase Date `15/09/26` pada aset D1 (Dinamis No 8); dibersihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan baca jumlah entri Changelog Asset D1, System Log Sarah Johnson, dan Activity Log sebelum aksi (disediakan tim FE/BE). Kolom Changed At diasersi dengan toleransi satu menit terhadap waktu aksi yang dicatat sesudah klik `[Save Details]`; jam server dan jam browser sinkron.
- State global: aset Company Targeted diubah; hook `after` memulihkan Company Targeted ke konfigurasi B3 dan aset D1 sampai D5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-277: Purchase Date diisi pertama kali: segmen Purchase Date berubah dari 0000 ke MMYY

1. Catat baseline jumlah entri Changelog Asset D1, System Log Sarah Johnson, dan Activity Log
2. Buka Fixed Asset > Assets > Registration
3. Klik `[Complete Detail]` pada aset D1
4. Isi Purchase Date `15/09/26`, Purchase Price `15000000`, dan unggah faktur `invoice.pdf` lalu klik `[Save Details]`, lalu catat waktu aksi
5. Verifikasi toast sukses `Success, asset details completed.` tampil
6. Buka Fixed Asset > Assets > All Assets > Detail D1
7. Verifikasi Asset ID D1 berubah dari `JKT/LAP/T490/0000/0000/1` menjadi `JKT/LAP/T490/0000/0926/1`; segmen selain Purchase Date tetap
8. Buka tab `Histori Aset`
9. Verifikasi entri teratas memuat Old Asset ID `JKT/LAP/T490/0000/0000/1`, New Asset ID `JKT/LAP/T490/0000/0926/1`, Reason `Data Update`, Changed At berisi tanggal dan jam aksi dalam format General Settings (dd/MM/yy, 24 jam, toleransi satu menit), dan Changed By `Sarah J`
10. Verifikasi banner info di Asset Detail berbunyi `Asset ID has been updated due to data completion. Previous ID: JKT/LAP/T490/0000/0000/1. Please reprint asset label if applicable.`

### TC-FA-CAID-254: Log cascade Data Update: entri per aset saat Purchase Date diisi

11. Buka Modal Changelog Asset pada Detail D1
12. Verifikasi Changelog aset bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0000/1`, dan New Value `JKT/LAP/T490/0000/0926/1`
13. Tutup Modal Changelog Asset
14. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
15. Verifikasi System Log aktor bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0000/1`, dan New Value `JKT/LAP/T490/0000/0926/1`
16. Buka Fixed Asset > Activity Log
17. Verifikasi Activity Log bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0000/1`, dan New Value `JKT/LAP/T490/0000/0926/1`

### TC-FA-CAID-283: Menyimpan ulang Purchase Date yang sama tidak mengubah Asset ID dan tidak menambah riwayat

18. Buka Fixed Asset > Assets > Registration dan klik `[Complete Detail]` pada aset D1
19. Simpan ulang dengan Purchase Date `15/09/26` tanpa perubahan lalu klik `[Save Details]`
20. Tunggu aksi selesai
21. Buka Fixed Asset > Assets > All Assets > Detail D1 > tab `Histori Aset`
22. Verifikasi Asset ID D1 tetap `JKT/LAP/T490/0000/0926/1`
23. Verifikasi jumlah entri tab `Histori Aset` tetap satu (tidak ada entri ganda)

### TC-FA-CAID-278: Purchase Date terisi diubah ke tanggal lain tidak memperbarui Asset ID

24. Buka Fixed Asset > Assets > Registration dan klik `[Complete Detail]` pada aset D3
25. Ubah Purchase Date menjadi `20/10/26` lalu klik `[Save Details]`
26. Tunggu aksi selesai
27. Buka Fixed Asset > Assets > All Assets > Detail D3 > tab `Histori Aset`
28. Verifikasi Asset ID D3 tetap `JKT/LAP/T490/HR/0926/3`
29. Verifikasi tidak ada entri riwayat Asset ID baru dan tidak ada banner

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-FA-CAID-254 dan TC-FA-CAID-283 mengikuti TC-FA-CAID-277 karena precondition keduanya adalah D1 yang diisi Purchase Date-nya oleh TC-FA-CAID-277; TC-FA-CAID-278 memakai D3 yang independen.
- Pembagian TC lintas spec: TC-FA-CAID-281 dan TC-FA-CAID-282 ada di spec 097 (`TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division`).
- Langkah penghubung: langkah 2, 18, 24 (buka halaman), 1 (baseline, S-12), 4 (catat waktu aksi), 13 (menutup modal), 20 dan 26 (tunggu aksi selesai sebelum pindah surface).
- Temuan untuk QA:
  - Langkah TC-FA-CAID-283 dan TC-FA-CAID-278 hanya menyebut Purchase Date dan `[Save Details]`, sedangkan TC-FA-CAID-277 juga mengisi Purchase Price dan faktur; spec mengikuti TC apa adanya.
  - TC-FA-CAID-254 tidak menyebut baseline jumlah entri log; baseline dicatat sebelum aksi (S-12).
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
