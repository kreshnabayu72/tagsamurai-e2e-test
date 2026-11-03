---
id: TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id
title: "Asset ID di All Assets, Detail Aset, dan Riwayat Asset ID"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-296
  - TC-FA-CAID-298
  - TC-FA-CAID-299
  - TC-FA-CAID-300
coverage:
  web: automated
---

# Asset ID di All Assets, Detail Aset, dan Riwayat Asset ID

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID untuk TC pertama.
- Data Pre-setup: Company Alpha baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan hook `beforeEach` suite: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`; General Settings Date Format `dd/MM/yy`, Time Format 24 jam (No 27). Antar TC, baseline B1 dan A1 sampai A5 dipulihkan lewat seed API. Untuk TC-FA-CAID-300, hook seed menyiapkan A1 yang sudah menjalani Transfer XFR-1 ke Group `Warehouse` (Asset ID `WH/LAP/T490/0926/1`, entri riwayat Reason `Transfer`, banner Transfer tampil); precondition TC, tidak diasersi selain banner.
- Data Dinamis: Group aset A1 menjadi `Warehouse` lewat seed (Dinamis No 9, dibuat di TC-FA-CAID-273); dibersihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md). Kolom Changed At diasersi dengan toleransi satu menit terhadap waktu aksi yang dicatat sesudah klik `[Save]`; jam server dan jam browser sinkron.
- State global: konfigurasi Company Alpha (Separator) dan Asset ID A1 sampai A3 diubah; hook `after` memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-296: Daftar All Assets dan Asset Detail menampilkan Asset ID baru setelah Save

1. Pilih Separator `- (Dash)` lalu klik `[Save]`
2. Tunggu aksi selesai
3. Buka Fixed Asset > Assets > All Assets dan perhatikan kolom Asset ID
4. Verifikasi kolom Asset ID menampilkan `JKT-LAP-T490-0926-1`, `JKT-LAP-T490-0926-2`, `JKT-LAP-T490-0000-3` untuk A1 sampai A3 tanpa reload tambahan
5. Buka Detail A1
6. Verifikasi header Asset Detail A1 menampilkan Asset ID `JKT-LAP-T490-0926-1`

### TC-FA-CAID-298: Riwayat Config Update dicatat per aset yang Asset ID-nya berubah dan tanpa banner

7. Pulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5 (seed API)
8. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`, lalu catat waktu aksi
9. Tunggu aksi selesai
10. Buka Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
11. Verifikasi entri teratas memuat Old Asset ID `JKT/LAP/T490/0926/1`, New Asset ID `JKT-LAP-T490-0926-1`, Reason `Config Update`, Changed At berisi tanggal dan jam aksi dalam format General Settings (dd/MM/yy, 24 jam, toleransi satu menit), dan Changed By `Sarah J`
12. Verifikasi tidak ada banner info pada Asset Detail A1 karena entri terbaru beralasan Config Update
13. Buka Detail A4 (Disposed) > tab `Histori Aset`
14. Verifikasi header Asset Detail A4 menampilkan Asset ID `JKT/LAP/T490/0926/4` (dibekukan)
15. Verifikasi Detail A4 tidak memuat entri riwayat baru

### TC-FA-CAID-299: Riwayat Asset ID ditampilkan dengan entri terbaru di atas dan entri lama immutable

16. Pulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5 (seed API)
17. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`
18. Tunggu aksi selesai
19. Pilih Separator `. (Dot)` lalu klik `[Save]`
20. Tunggu aksi selesai
21. Buka Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
22. Verifikasi entri teratas memuat Old Asset ID `JKT-LAP-T490-0926-1`, New Asset ID `JKT.LAP.T490.0926.1`, Reason `Config Update`
23. Verifikasi entri kedua memuat Old Asset ID `JKT/LAP/T490/0926/1`, New Asset ID `JKT-LAP-T490-0926-1`, Reason `Config Update`, tidak berubah oleh perubahan berikutnya
24. Verifikasi hanya ada dua entri karena penerbitan Asset ID awal tidak punya entri

### TC-FA-CAID-300: Banner info hilang saat entri riwayat terbaru berganti menjadi Config Update

25. Pulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5, dengan A1 sudah menjalani Transfer XFR-1 ke Group `Warehouse` (seed API)
26. Buka Fixed Asset > Assets > All Assets > Detail A1 dan perhatikan banner
27. Verifikasi banner Transfer tampil sebelum Save
28. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`
29. Tunggu aksi selesai
30. Buka kembali Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
31. Verifikasi entri terbaru beralasan Config Update
32. Verifikasi banner info tidak tampil

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Dependensi TC-FA-CAID-300 pada TC-FA-CAID-273 dijalankan lewat seeding API (S-04): Transfer A1 ke Group `Warehouse` disiapkan oleh seed, bukan oleh UI spec ini; spec 088 menguji Transfer itu sendiri.
- Langkah penghubung: langkah 3, 10, 21, 26, 30 (buka halaman), 2, 9, 18, 20, 29 (tunggu aksi selesai sebelum pindah surface), 7, 16, 25 (pemulihan Company Alpha antar TC lewat seed), 8 (catat waktu aksi).
- Langkah 14 adalah anchor positif untuk asersi absence pada langkah 15; Expected TC-FA-CAID-298 menyebut Asset ID Disposed dibekukan, jadi langkah 14 memverifikasi klausa itu.
- Temuan untuk QA:
  - Expected TC-FA-CAID-300 "banner Transfer tampil" tidak menyebut teksnya; spec memverifikasi tampilnya banner tanpa teks.
  - Langkah TC-FA-CAID-300 tidak membuka tab `Histori Aset`, padahal Expected menyebut entri terbaru; spec membukanya sebagai langkah penghubung (S-14).
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
