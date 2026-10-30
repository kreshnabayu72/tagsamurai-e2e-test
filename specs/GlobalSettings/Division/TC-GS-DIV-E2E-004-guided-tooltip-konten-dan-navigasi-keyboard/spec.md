---
id: TC-GS-DIV-E2E-004-guided-tooltip-konten-dan-navigasi-keyboard
title: "Guided Tooltip Tab Division: Konten 3 Step dan Navigasi Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-10
  - TC-GS-DIV-16
coverage:
  web: automated
---

# Guided Tooltip Tab Division: Konten 3 Step dan Navigasi Keyboard

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor yang dimodelkan lewat payload izin mock: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD`.
- Kebutuhan mock (respons yang dipaksa; API pendukung di luar sumber modul disediakan tim FE):
  - Respons sesi/profil dan payload izin (disediakan tim FE; API di luar sumber modul): Total Control (semua aksi Division, termasuk Create sehingga `[+ Division]` tampil).
  - Respons daftar Division: minimal 6 baris Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) sehingga tabel Division List, `[+ Division]`, dan icon `[Changelog]` ter-render.
  - Stream SSE tab Division (PRD `division.md` bagian Sync + Realtime; LLD `API/low-level-design.md` L159, L256, L347 hanya menyebut event `division.created`, `division.updated`, `division.deleted` tanpa path endpoint, sehingga path stream disediakan tim FE): koneksi stream di-mock tetap terbuka dan tidak mengirim event apa pun selama spec, sehingga tidak ada refetch atau perubahan data tabel.
  - Respons preferensi Guided Tooltip untuk flag `guided_tooltip_seen_gs-division`: belum ada pada seluruh spec (TC-GS-DIV-10 dan TC-GS-DIV-16 mensyaratkan flag belum ada); penyimpanan flag oleh `[Skip]` atau `Esc` tidak mengubah respons mock selama spec berjalan. Mock mencatat permintaan penyimpanan flag `seen` untuk `page_key` `gs-division` sehingga dapat diasersi (langkah 24); nama endpoint ditentukan tim FE berdasarkan `foundation/functions/guided-tooltip.md`.
- Tidak ada data backend atau state global yang diubah, sehingga tidak ada cleanup selain melepas mock di hook `after`.

## Test Steps

### TC-GS-DIV-10: Konten 3 step Guided Tooltip halaman Division sesuai urutan

1. Terapkan mock sesi Total Control dengan flag `guided_tooltip_seen_gs-division` belum ada
2. Buka Global Settings > User > Tab Division untuk kunjungan pertama
3. Verifikasi Step 1 menyorot Tombol `[+ Division]`
4. Verifikasi Step 1 Title `Add Division`
5. Verifikasi Step 1 Description `Create a new division to group the staff accounts in your organization.`
6. Klik `[Next]`
7. Verifikasi Step 2 menyorot Tabel Division List
8. Verifikasi Step 2 Title `Division Table`
9. Verifikasi Step 2 Description `Browse and manage all divisions in your organization from this table.`
10. Klik `[Next]`
11. Verifikasi Step 3 menyorot Icon `[Changelog]`
12. Verifikasi Step 3 Title `Changelog Audit`
13. Verifikasi Step 3 Description `Review the history of changes made to divisions.`

### TC-GS-DIV-16: Keyboard pada walkthrough: Esc, Enter, panah kanan, panah kiri

14. Muat ulang Tab Division untuk kunjungan pertama (flag mock tetap belum ada)
15. Verifikasi tooltip mendapat keyboard focus saat walkthrough aktif
16. Tekan Enter
17. Verifikasi Enter berpindah ke Step 2
18. Tekan panah kanan
19. Verifikasi panah kanan berpindah ke Step 3
20. Tekan panah kiri
21. Verifikasi panah kiri kembali ke Step 2
22. Tekan Esc
23. Verifikasi Esc menutup walkthrough
24. Verifikasi mock menerima permintaan penyimpanan flag `seen` untuk `page_key` `gs-division`

## Notes

- Mode: mock. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. TC-GS-DIV-10 berakhir di Step 3 tanpa menutup walkthrough; langkah 14 memuat ulang tab supaya TC-GS-DIV-16 mulai dari kunjungan pertama (Step 1) dengan flag mock yang masih belum ada.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (mock sesi dan flag awal) dan 14 (muat ulang tab untuk kunjungan pertama berikutnya).
- Perilaku `[Skip]`, overlay, `[Done]`, `[Back]`, replay `[?]`, dan resize diuji di spec `TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize`; tombol `[Done]` pada Step 3 tidak diasersi di spec ini karena tidak ada di Expected Result TC-GS-DIV-10 dan TC-GS-DIV-16.
- Temuan untuk QA:
  - TC-GS-DIV-16 langkah 1 sampai 5 tidak menyebut Step yang dituju tiap tombol; spec mengikuti urutan TC (Enter ke Step 2, panah kanan ke Step 3, panah kiri ke Step 2, Esc) berdasarkan Expected Result b ("Enter dan panah kanan = Next, panah kiri = Back").
  - TC-GS-DIV-16 Expected Result c ("flag `seen` tersimpan") tidak memberi cara cek; di mode mock spec membaca permintaan simpan yang diterima mock (langkah 24). Endpoint tidak disebut di TC maupun PRD Division; ditentukan tim FE.
  - TC-GS-DIV-10 menyebut target Step 2 sebagai `Tabel Division List (T-DIV-01)`; selector konkret ditentukan tim FE.
