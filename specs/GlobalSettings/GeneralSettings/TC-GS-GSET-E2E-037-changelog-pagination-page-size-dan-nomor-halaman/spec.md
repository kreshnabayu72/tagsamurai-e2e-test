---
id: TC-GS-GSET-E2E-037-changelog-pagination-page-size-dan-nomor-halaman
title: "Changelog General Settings: Pagination, Page Size, Navigasi Halaman, dan Input Nomor Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-102
  - TC-GS-GSET-180
coverage:
  web: automated
---

# Changelog General Settings: Pagination, Page Size, Navigasi Halaman, dan Input Nomor Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10).
- Seeding di hook `before` (precondition TC "minimal 26 baris", Data Uji Dinamis No 4): 28 PUT berurutan ke `/v2/enterprise-management/general-settings` (full-replace, `global-settings/general-settings/API/openapi.yaml`) oleh sesi API Budi Santoso; tiap PUT mengubah tepat satu field sehingga menambah satu baris Changelog: 27 perubahan `sessionIdleTimeout` bergantian antara 60 dan 120 menit (dimulai dari 30 ke 60), lalu satu perubahan kembali ke 30 menit. Jumlah baris dari seeding ini 28 (N dari seeding, bagian 8b butir 10 konvensi), sehingga Changelog memuat sedikitnya 26 baris: halaman 1, 2, dan 3 pada page size 10 tersedia, dan page size 25 menampilkan tepat 25 baris pada halaman 1. Total entri Changelog tidak diasersi sebagai angka tetap (audit trail permanen; entri dari spec lain ikut menambah jumlah).
- Data uji: page size `10`, `25`, `50`, `100`; nomor halaman `2` dan `3`.
- State yang diubah dan dipulihkan: page size dan halaman aktif Modal Changelog; ditutup bersama modal (membuka kembali Modal Changelog menampilkan kondisi default: halaman 1, page size 10, PRD §4.2b). Tidak ada state global yang berubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-102: Pagination Changelog: default 10, page size, dan navigasi

1. Klik icon Changelog di pojok kanan atas halaman
2. Verifikasi page size default pada Pagination adalah 10
3. Verifikasi halaman 1 menampilkan tepat 10 baris
4. Klik dropdown page size pada Pagination
5. Verifikasi opsi page size 10, 25, 50, dan 100
6. Pilih page size 10
7. Klik halaman berikutnya
8. Verifikasi halaman 2 aktif pada Pagination
9. Verifikasi halaman 2 menampilkan tepat 10 baris
10. Klik halaman sebelumnya
11. Verifikasi halaman 1 aktif pada Pagination
12. Ubah page size ke 25
13. Verifikasi halaman 1 menampilkan tepat 25 baris
14. Ubah page size ke 50
15. Verifikasi halaman 1 menampilkan lebih dari 25 baris dan paling banyak 50 baris
16. Ubah page size ke 100
17. Verifikasi halaman 1 menampilkan lebih dari 25 baris dan paling banyak 100 baris

### TC-GS-GSET-180: Pagination Changelog: input nomor halaman langsung lalu Enter

18. Ubah page size ke 10
19. Ketik `2` pada input nomor halaman, tekan `Enter`
20. Verifikasi langsung berpindah ke halaman 2
21. Ketik `3` pada input nomor halaman, tekan `Enter`
22. Verifikasi langsung berpindah ke halaman 3

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (data Changelog dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (102, 180) dipertahankan. Modal Changelog dibuka sekali di langkah 1 dan dipakai TC-180 (langkah 1 TC-180 "Buka Modal Changelog" dipenuhi langkah 1).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog), langkah 6 (mengembalikan page size ke 10 setelah verifikasi daftar opsi), dan langkah 18 (page size 10 agar halaman 2 dan 3 tersedia pada TC-180; jumlah baris dari seeding 28 sehingga ada 3 halaman).
- Asersi tambahan (konkretisasi, S-03): langkah 3, 9, 13, 15, dan 17 mengasersi jumlah baris per page size; Expected TC-102 hanya menyebut default 10, daftar opsi, dan navigasi, sedangkan langkah 4 TC menyebut perubahan page size ke 25, 50, dan 100 tanpa Expected. Langkah 15 dan 17 memakai rentang ("lebih dari 25 dan paling banyak 50 atau 100") karena total entri tidak tetap; batas bawah 25 menjamin hasil lebih banyak dari page size 25 dan bergantung pada seeding 28 baris. Langkah 8 dan 11 memakai indikator halaman aktif karena baris yang sama-sama bertanggal menit yang sama tidak membedakan halaman.
- Dipisah dari spec 038, 039, dan 053 karena gabungan langkahnya melewati batas ukuran jauh (22 + 52 + 35 + 45 = 154 langkah) dan seeding berbeda (spec ini 28 PUT; spec 038 delapan PUT; spec 039 dan 053 masing-masing 17 PUT).
- Pembagian TC lintas spec: TC-GS-GSET-157 (pagination bersama Search dan Filter) ada di spec 039 dan TC-GS-GSET-181 (pindah halaman mempertahankan Search, Filter, Sort) di spec 053; TC-GS-GSET-153 (page size bersama kombinasi) di spec 038.
- Temuan untuk QA:
  - TC-GS-GSET-102: langkah 4 (ubah page size ke 25, 50, 100) tidak punya Expected; hanya daftar opsi (butir b) dan navigasi (butir c) yang dinyatakan. Spec menambahkan asersi jumlah baris per page size sebagai konkretisasi (Notes di atas).
  - TC-GS-GSET-102 butir c ("menampilkan halaman yang sesuai") tidak menyebut cara mengenali halaman; spec memakai indikator halaman aktif pada Pagination.
  - TC-GS-GSET-180: TC tidak menyebut posisi atau label input nomor halaman; spec menyebutnya "input nomor halaman".
