---
id: TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog
title: "Empty State Tabel Measurement dan Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-11
  - TC-GS-UOM-12
  - TC-GS-UOM-175
  - TC-GS-UOM-10
  - TC-GS-UOM-174
coverage:
  web: automated
---

# Empty State Tabel Measurement dan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1 (awal spec): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before`. Dipakai untuk TC-GS-UOM-11, TC-GS-UOM-12, dan TC-GS-UOM-175.
- Akun aktor 2 (ganti akun di langkah 17 sampai 19): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (kredensial `Spectra.env.GS_CLIENTC_TC_PASSWORD`). Dipakai untuk TC-GS-UOM-10 dan TC-GS-UOM-174. Client C adalah client tanpa Measurement dan tanpa entri Changelog (data environment tetap; tidak boleh ada seeding Measurement di client ini).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir di Client C. Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` dan `GS_CLIENTC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Client A (hanya dibaca): Pre-setup Client A dan Population D-01 (di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`), Changelog Client A memiliki sedikitnya satu entri (data yang sudah ada dari seeding Population), sehingga pencarian `zzqx` pada Changelog menghasilkan `No results found`, bukan `No changelog yet`. Spec tidak membuat atau mengubah data backend; tidak ada cleanup data.
- Guided Tooltip: flag halaman Measurement untuk kedua akun aktor mengikuti pernyataan hook suite di `suite.md`.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite untuk akun default; layar untuk Client C dibuka lewat langkah spec setelah login.
- State global yang diubah: tidak ada. State Search dan Filter tabel dibersihkan lewat langkah pemulihan di tengah spec.

## Test Steps

### TC-GS-UOM-11: Empty state tabel saat Search tidak menemukan hasil

1. Ketik Search `zzqx`, tekan Enter
2. Verifikasi Illustration tampil
3. Verifikasi Title `No results found`
4. Verifikasi Description `Try adjusting your search or filter.`
5. Klik `(←)` pada kotak Search

### TC-GS-UOM-12: Empty state tabel saat Filter Last Updated tidak menemukan hasil

6. Klik Filter
7. Pilih rentang Last Updated 01 Jan 2020 – 02 Jan 2020
8. Klik [Apply]
9. Verifikasi Title `No results found`
10. Verifikasi Description `Try adjusting your search or filter.`
11. Klik Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-UOM-175: Empty state Modal Changelog saat Search tidak menemukan hasil

12. Klik icon Changelog
13. Ketik Search `zzqx` pada Modal Changelog, tekan Enter
14. Verifikasi Title `No results found`
15. Verifikasi Description `Try adjusting your search or filter.`
16. Tutup Modal Changelog lewat `✕` di header

### Ganti akun ke Client C

17. Logout dari Total Control Client A
18. Login sebagai Total Control Client C
19. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-10: Empty state tabel saat belum ada Measurement

20. Verifikasi Illustration tampil
21. Verifikasi Title `No units yet`
22. Verifikasi Description `Get started by creating your first measurement unit.`
23. Verifikasi tidak ada tombol CTA tambahan di empty state
24. Verifikasi `[+ Unit]` tetap tampil di Table Tools

### TC-GS-UOM-174: Empty state Modal Changelog saat belum ada riwayat

25. Klik icon Changelog
26. Verifikasi Title `No changelog yet`
27. Verifikasi Description `Activities and changes will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-UOM-175 (Client A) dimajukan sebelum TC-GS-UOM-10 dan TC-GS-UOM-174 (Client C) supaya semua TC Client A selesai sebelum ganti akun.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5 (mengosongkan Search), 11 (membersihkan Filter Last Updated lewat `[Clear Field]` dan `[Apply]`), 16 (menutup Modal Changelog), dan 17 sampai 19 (ganti akun ke Client C dan membuka layar Measurement).
- Pada TC-GS-UOM-10, absence tombol CTA tambahan (langkah 23) memakai Title dan Description empty state (langkah 21 dan 22) sebagai anchor positif pada surface yang sama.
- Spec memakai dua entity (Client A lalu Client C) dengan Step ganti akun eksplisit; bagian Client C tetap bermakna walau bagian Client A gagal.
- Temuan untuk QA: TC-GS-UOM-175 tidak menyebut precondition bahwa Changelog Client A berisi entri; tanpa entri, pencarian `zzqx` akan menampilkan `No changelog yet` dan bukan `No results found`. Spec mencatat kebutuhan itu di Prerequisites.
