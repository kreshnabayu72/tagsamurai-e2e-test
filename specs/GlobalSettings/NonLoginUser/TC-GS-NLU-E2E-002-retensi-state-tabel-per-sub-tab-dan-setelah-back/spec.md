---
id: TC-GS-NLU-E2E-002-retensi-state-tabel-per-sub-tab-dan-setelah-back
title: "Retensi state tabel per sub-tab dan setelah Back atau Refresh"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-6
  - TC-GS-NLU-253
  - TC-GS-NLU-254
coverage:
  web: automated
---

# Retensi state tabel per sub-tab dan setelah Back atau Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza, Default User entitas), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk akun aktor sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: Non-Login User Rina Marlina (No. 11, Driver, Logistics) hanya dibaca; kata kunci `Rina` hanya cocok dengan baris Rina Marlina pada sub-tab Non-Login User.
- Spec hanya membaca. State UI yang diubah (Search dan sort Division) dipulihkan lewat langkah penghubung; tidak ada state global yang diubah. Persistensi Search, sort, dan halaman setelah muat ulang mengikuti PRD (mekanisme penyimpanan tidak diasumsikan di spec).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-6: State tabel dipertahankan per sub-tab saat pindah sub-tab lalu kembali

1. Klik icon Search, ketik Search `Rina`, tekan Enter
2. Verifikasi baris Rina Marlina tampil di tabel
3. Klik sub-tab `Login User`
4. Verifikasi kotak Search sub-tab `Login User` tidak berisi keyword `Rina`
5. Klik sub-tab `Non-Login User`
6. Verifikasi kotak Search masih terisi keyword `Rina`
7. Verifikasi tabel Non-Login User tetap tersaring ke Rina Marlina
8. Klik `(←)` pada kotak Search

### TC-GS-NLU-253: Kembali ke list lewat Back browser mempertahankan Search yang aktif

9. Klik icon Search, ketik Search `Rina`, tekan Enter
10. Klik Name Rina Marlina
11. Klik tombol Back browser
12. Verifikasi List Non-Login User tampil kembali dengan keyword `Rina` terisi di kotak Search
13. Verifikasi tabel masih tersaring ke Rina Marlina
14. Klik `(←)` pada kotak Search

### TC-GS-NLU-254: Refresh halaman list mempertahankan Search Filter Sort dan paginasi

15. Klik icon Search, ketik Search `Rina`, tekan Enter
16. Klik header kolom Division satu kali hingga urutan ascending
17. Muat ulang halaman (F5)
18. Verifikasi keyword `Rina` tetap terisi di kotak Search
19. Verifikasi sort kolom Division ascending tetap (indikator sort pada header Division)
20. Verifikasi halaman aktif tetap halaman 1
21. Kembalikan sort ke default Name A-Z, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): langkah 8, 14, 21 (mengosongkan Search dan mengembalikan sort sebelum TC berikutnya).
- Temuan untuk QA:
  - TC-GS-NLU-6 Expected b ("State Search sub-tab Login User tidak ikut berubah") tidak menyebut keadaan awal Search sub-tab Login User. Spec mengasumsikan kotak Search sub-tab Login User kosong sebelum uji dan mengasersi tidak berisi `Rina`.
  - TC-GS-NLU-254 Expected ("Keyword, sort, dan halaman aktif tetap") tidak menyebut halaman selain halaman 1. Search `Rina` hanya menghasilkan satu baris, sehingga sort diasersi lewat indikator header (bukan urutan baris, S-11) dan halaman aktif diasersi sebagai halaman 1.
  - TC-GS-NLU-254 tidak menyebut siklus klik sort. Spec mengasumsikan satu klik pada header Division menghasilkan ascending.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
