---
id: TC-AC-SU-E2E-004-navigasi-ke-detail-loading-state-dan-no-result
title: "User List: Navigasi ke Detail User, Loading State Tabel, dan No Result State Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-14
  - TC-AC-SU-15
  - TC-AC-SU-17
  - TC-AC-SU-19
coverage:
  web: automated
---

# User List: Navigasi ke Detail User, Loading State Tabel, dan No Result State Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-14, 15 | `John Doe` | `John Doe {runId}-004` | `johndoe+{runId}-004@qwertysystem.net` | Activated, Active |

- Kemampuan teknis tambahan: `Spectra.intercept()` untuk menahan respons request daftar user sementara (TC-AC-SU-17); intercept dilepas pada langkah asersi akhir TC itu dan dilepas di hook `after` bila spec gagal di tengah. Menahan respons hanya untuk mengamati Loading dan bukan fault injection.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-19: No result state saat Search tanpa hasil

1. Ketik Search `zzqxyz`, tekan Enter
2. Verifikasi empty state: Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
3. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SU-17: Loading state tabel User List

4. Tahan respons request daftar user dengan intercept
5. Muat ulang halaman Settings > User dengan F5
6. Verifikasi 5 skeleton rows tampil
7. Verifikasi kolom skeleton sesuai layout aktual
8. Lepas tahanan respons
9. Verifikasi skeleton rows hilang dan baris data tampil setelah data diterima

### TC-AC-SU-15: Navigasi ke Detail via row action Detail

10. Ketik Search `John Doe {runId}-004`, tekan Enter
11. Klik (⋯) baris `John Doe {runId}-004`
12. Klik `Detail`
13. Verifikasi navigasi ke Settings > User > Detail milik `John Doe {runId}-004`
14. Verifikasi Tab Role aktif
15. Verifikasi sub-tab Global Role aktif
16. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-14: Navigasi ke Detail via klik Name

17. Klik teks Name `John Doe {runId}-004`
18. Verifikasi navigasi ke Settings > User > Detail milik `John Doe {runId}-004` pada tab yang sama (same-tab)
19. Verifikasi Tab Role aktif
20. Verifikasi sub-tab Global Role aktif
21. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
22. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 3 dan 22 (reset Search), langkah 10 (Search untuk menemukan baris target, R-16), langkah 16 dan 21 (kembali ke daftar). Muat ulang F5 pada TC-AC-SU-17 menggantikan "Buka Settings > User" karena layar awal sudah dibuka hook `beforeEach` suite.
- Urutan TC dalam spec: 19, 17, 15, 14 (No result dan Loading di daftar lebih dulu; navigasi ke Detail terakhir karena meninggalkan halaman, S-10).
- Temuan untuk QA:
  - TC-AC-SU-17 tidak menyebut mekanisme penundaan respons selain "network throttle"; spec memakai intercept respons daftar user (disediakan tim FE).
  - TC-AC-SU-14 "navigasi same-tab" tidak menyebut cara cek; spec mengasersi tidak ada tab browser baru.
  - Nama user TC (`John Doe`) dipakai sebagai nama bersuffix `{runId}-004` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
