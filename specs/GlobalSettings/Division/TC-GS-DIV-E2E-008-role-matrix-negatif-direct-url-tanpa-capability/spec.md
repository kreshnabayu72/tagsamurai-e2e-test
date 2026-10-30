---
id: TC-GS-DIV-E2E-008-role-matrix-negatif-direct-url-tanpa-capability
title: "Role Matrix Negatif: Akses Langsung Tab Division Tanpa Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-25
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung Tab Division Tanpa Capability

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-DIV-25 | Tanpa Capability (tanpa capability Manage user and role) | Fajar Nugroho | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Akun pembantu: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dipakai untuk menyalin URL Tab Division (langkah 1 TC-GS-DIV-25). Login Total Control dilakukan di hook `before` (akun aktor pertama spec); langkah ganti akun ke Tanpa Capability ditulis eksplisit di Test Steps. Karena spec berakhir di akun Tanpa Capability, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` dan `GS_NOCAP_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Division (6 Division, data environment tetap) tersedia sehingga ketiadaan data Division di layar disebabkan oleh izin, bukan data kosong. Spec tidak membuat atau menghapus data.
- Kemampuan teknis: membaca URL dari address bar dan menempelkannya sebagai navigasi langsung (URL Tab Division Global Settings > User, Data Uji TC-GS-DIV-25) oleh sesi akun Tanpa Capability.
- Guided Tooltip: tidak relevan karena aktor Tanpa Capability tidak dapat membuka Tab Division, dan Total Control hanya membuka tab untuk menyalin URL; hook `before` menyetel flag `guided_tooltip_seen_gs-division` akun Total Control ke true supaya walkthrough tidak menutupi layar dan hook `after` memulihkan nilai awal. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- State global yang diubah: hanya flag Guided Tooltip akun Total Control (dipulihkan seperti di atas).

## Test Steps

### TC-GS-DIV-25: Akses langsung ke Tab Division tanpa capability

1. Buka Global Settings > User > Tab Division lalu salin URL Tab Division dari address bar (akun Total Control)
2. Logout dari Total Control
3. Login sebagai Tanpa Capability
4. Tempel URL Tab Division yang disalin pada langkah 1 di address bar lalu tekan Enter
5. Verifikasi toast error `You don't have permission to do this.`
6. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi
7. Verifikasi tidak ada redirect ke halaman terpisah
8. Verifikasi data Division tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 membuka layar karena menyalin URL Tab Division dari address bar adalah Langkah Uji TC-GS-DIV-25.
- Spec Role Matrix negatif (bagian 3a konvensi) untuk satu role. Role negatif lain tidak ditulis di sini karena tidak ada TC sumbernya; visibilitas elemen per role diuji di spec `TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 dan 3 (ganti akun dari Total Control ke Tanpa Capability).
- Langkah 5 sampai 7 (toast dan UI di-refresh) menjadi anchor bahwa halaman sudah selesai diproses sebelum asersi data Division tidak tampil pada langkah 8.
- Temuan untuk QA:
  - TC-GS-DIV-25 Expected b ("UI di-refresh sehingga elemen yang tidak berhak tersembunyi, tanpa redirect ke halaman terpisah") dipecah menjadi dua `Verifikasi` (langkah 6 dan 7). Elemen yang dimaksud tidak disebut; PRD §4.8 menyebut Tab `Division` Hidden bagi aktor tanpa capability, tetapi TC tidak menyatakan halaman apa yang tampil sesudah refresh.
