---
id: TC-GS-BRAND-E2E-004-empty-state-tabel-dan-changelog
title: "Empty State Tabel Brand dan Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-15
  - TC-GS-BRAND-16
  - TC-GS-BRAND-171
  - TC-GS-BRAND-14
  - TC-GS-BRAND-170
coverage:
  web: automated
---

# Empty State Tabel Brand dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1 (awal spec): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before`. Dipakai untuk TC-GS-BRAND-15, TC-GS-BRAND-16, dan TC-GS-BRAND-171.
- Akun aktor 2 (ganti akun di langkah 20 dan 21): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (kredensial `Spectra.env.GS_CLIENTC_TC_PASSWORD`). Dipakai untuk TC-GS-BRAND-14 dan TC-GS-BRAND-170. Client C adalah client tanpa Brand dan tanpa Changelog (data environment tetap; tidak boleh ada seeding Brand di client ini).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir di Client C. Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` dan `GS_CLIENTC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (12 brand, data environment tetap; hanya dibaca). Changelog Client A memiliki minimal 1 aktivitas (data Pre-setup; precondition TC-GS-BRAND-171) sehingga pencarian `zzqx` menghasilkan `No results found`, bukan `No changelog yet`.
- Spec tidak membuat atau mengubah data backend; tidak ada cleanup data.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` untuk kedua akun lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal.
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). Format tanggal mengikuti General Settings yang berlaku di Client A (tidak diubah). State Search dan Filter tabel dibersihkan lewat langkah pemulihan di tengah spec.

## Test Steps

### TC-GS-BRAND-15: Empty state tabel saat Search tidak menemukan hasil

1. Buka Global Settings > Master Reference dari sidebar → tab Brand tampil
2. Klik icon Search
3. Ketik `zzqx`
4. Tekan Enter
5. Verifikasi Illustration tampil
6. Verifikasi Title `No results found`
7. Verifikasi Description `Try adjusting your search or filter.`
8. Hapus keyword Search sehingga tabel kembali menampilkan brand

### TC-GS-BRAND-16: Empty state tabel saat Filter Last Updated tidak menemukan hasil

9. Klik Filter
10. Pilih rentang Last Updated 01 Jan 2020 – 02 Jan 2020
11. Klik [Apply]
12. Verifikasi Title `No results found`
13. Verifikasi Description `Try adjusting your search or filter.`
14. Reset Filter Last Updated sehingga tabel kembali menampilkan brand

### TC-GS-BRAND-171: Empty state Changelog saat search tidak menemukan hasil

15. Buka Changelog dengan mengklik icon Changelog
16. Search `zzqx`, tekan Enter
17. Verifikasi Title `No results found`
18. Verifikasi Description `Try adjusting your search or filter.`
19. Tutup Modal Changelog dengan `✕` di header

### Ganti akun ke Client C

20. Logout dari Total Control Client A
21. Login sebagai Total Control Client C

### TC-GS-BRAND-14: Empty state tabel saat belum ada Brand

22. Buka Global Settings > Master Reference > Brand
23. Verifikasi Illustration tampil
24. Verifikasi Title `No brands yet`
25. Verifikasi Description `Get started by creating your first brand.`
26. Verifikasi `[+ Brand]` tetap tampil di Table Tools

### TC-GS-BRAND-170: Empty state Changelog saat belum ada aktivitas

27. Klik icon Changelog
28. Verifikasi Title `No changelog yet`
29. Verifikasi Description `Activities and changes will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-BRAND-171 (Client A) dimajukan sebelum TC-GS-BRAND-14 dan TC-GS-BRAND-170 (Client C) supaya semua TC Client A selesai sebelum ganti akun.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 (hapus keyword Search supaya TC-GS-BRAND-16 berasal dari Filter saja), 14 (reset Filter Last Updated), 19 (tutup Modal Changelog), 20 dan 21 (ganti akun ke Client C).
- Spec memakai dua entity (Client A lalu Client C) dengan Step ganti akun eksplisit; bagian Client C tetap bermakna walau bagian Client A gagal.
