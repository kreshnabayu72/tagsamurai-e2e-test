---
id: TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten
title: "Mutasi Division: Isi, Ganti, Log Cascade, dan Idempoten"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-285
  - TC-FA-CAID-255
  - TC-FA-CAID-286
  - TC-FA-CAID-302
coverage:
  web: automated
---

# Mutasi Division: Isi, Ganti, Log Cascade, dan Idempoten

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Targeted (Pre-setup No 29; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE; pengguna Sarah Johnson), password `Spectra.env.FA_TARGETED_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Targeted (No 29): hook `before` men-seed konfigurasi B3 (Slash; Group, Category, Asset Name, Division, Purchase Date, Increment) dan aset Draft D1 sampai D3 (D2 `JKT/LAP/T490/0000/0926/2` dengan Division kosong, D3 `JKT/LAP/T490/HR/0926/3` dengan Division `Human Resources`), Active D4, Waiting for Approval D5; Division `Human Resources` (Code `HR`) dan `Finance` (Code `FIN`); General Settings Date Format `dd/MM/yy`, Time Format 24 jam (No 27).
- Data Dinamis: Division aset D2 menjadi `Human Resources` (Dinamis No 11); dibersihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan baca jumlah entri Changelog Asset D2, System Log Sarah Johnson, dan Activity Log sebelum aksi (disediakan tim FE/BE). Kolom Changed At diasersi dengan toleransi satu menit terhadap waktu aksi yang dicatat sesudah simpan Edit Draft; jam server dan jam browser sinkron.
- State global: aset Company Targeted diubah; hook `after` memulihkan Company Targeted ke konfigurasi B3 dan aset D1 sampai D5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-285: Division diisi pada aset yang sebelumnya kosong: segmen Division berubah dari 0000 ke kode Division

1. Catat baseline jumlah entri Changelog Asset D2, System Log Sarah Johnson, dan Activity Log
2. Buka Fixed Asset > Assets > Registration
3. Edit Draft aset D2: pilih Division `Human Resources` lalu simpan, lalu catat waktu aksi
4. Tunggu aksi selesai
5. Buka Fixed Asset > Assets > All Assets > Detail D2
6. Verifikasi Asset ID D2 berubah dari `JKT/LAP/T490/0000/0926/2` menjadi `JKT/LAP/T490/HR/0926/2`; segmen lain tetap
7. Buka tab `Histori Aset`
8. Verifikasi entri teratas memuat Old Asset ID `JKT/LAP/T490/0000/0926/2`, New Asset ID `JKT/LAP/T490/HR/0926/2`, Reason `Division Change`, Changed At berisi tanggal dan jam aksi dalam format General Settings (dd/MM/yy, 24 jam, toleransi satu menit), dan Changed By `Sarah J`
9. Verifikasi banner info di Asset Detail berbunyi `Asset ID has been updated due to division change. Previous ID: JKT/LAP/T490/0000/0926/2. Please reprint asset label if applicable.`

### TC-FA-CAID-255: Log cascade Division Change: entri per aset saat Division berubah

10. Buka Modal Changelog Asset pada Detail D2
11. Verifikasi Changelog aset bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0926/2`, dan New Value `JKT/LAP/T490/HR/0926/2` (segmen Division berubah dari `0000` menjadi `HR`)
12. Tutup Modal Changelog Asset
13. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
14. Verifikasi System Log aktor bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0926/2`, dan New Value `JKT/LAP/T490/HR/0926/2`
15. Buka Fixed Asset > Activity Log
16. Verifikasi Activity Log bertambah satu entri dibanding baseline dengan Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0000/0926/2`, dan New Value `JKT/LAP/T490/HR/0926/2`

### TC-FA-CAID-302: Menyimpan ulang Division yang sama tidak mengubah Asset ID dan tidak menambah riwayat

17. Buka Fixed Asset > Assets > Registration
18. Edit Draft aset D2: simpan ulang dengan Division `Human Resources` tanpa perubahan
19. Tunggu aksi selesai
20. Buka Fixed Asset > Assets > All Assets > Detail D2 > tab `Histori Aset`
21. Verifikasi Asset ID D2 tetap `JKT/LAP/T490/HR/0926/2`
22. Verifikasi jumlah entri tab `Histori Aset` tidak bertambah dari satu

### TC-FA-CAID-286: Division diganti pada aset: segmen Division berubah ke kode Division baru

23. Buka Fixed Asset > Assets > Registration
24. Edit Draft aset D3: ganti Division dari `Human Resources` menjadi `Finance` lalu simpan
25. Tunggu aksi selesai
26. Buka Fixed Asset > Assets > All Assets > Detail D3 > tab `Histori Aset`
27. Verifikasi Asset ID D3 berubah dari `JKT/LAP/T490/HR/0926/3` menjadi `JKT/LAP/T490/FIN/0926/3`
28. Verifikasi entri riwayat dengan Reason `Division Change` tercatat

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-FA-CAID-255 dan TC-FA-CAID-302 mengikuti TC-FA-CAID-285 karena precondition keduanya adalah D2 yang diisi Division-nya oleh TC-FA-CAID-285; TC-FA-CAID-286 memakai D3 yang independen dan ditulis terakhir.
- Pembagian TC lintas spec: TC-FA-CAID-287 dan TC-FA-CAID-301 ada di spec 097 (`TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division`).
- Langkah penghubung: langkah 2, 17, 23 (buka halaman), 1 (baseline, S-12), 3 (catat waktu aksi), 12 (menutup modal), 4, 19, 25 (tunggu aksi selesai sebelum pindah surface).
- Temuan untuk QA:
  - TC-FA-CAID-255 tidak menyebut baseline jumlah entri log; baseline dicatat sebelum aksi (S-12).
  - Email akun Total Control Company Targeted tidak tertulis di Pre-setup TC.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
