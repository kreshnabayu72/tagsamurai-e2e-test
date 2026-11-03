---
id: TC-AC-ACC-E2E-054-create-pakai-ulang-client-code-dan-email-client-dihapus-tcp
title: "Create Client: Client Code dan Email Default User Milik Client yang Sudah Dihapus Dipakai Ulang (Total Control)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-499
  - TC-AC-ACC-500
coverage:
  web: automated
---

# Create Client: Client Code dan Email Default User Milik Client yang Sudah Dihapus Dipakai Ulang (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-054@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Hook `before` men-seed lewat API lalu men-soft-delete Client `PT Kode Dihapus {runId}-054` (setara C-CRE-1) dengan Client Code `DHP-015` (literal sesuai TC; hook `before` juga menghapus sisa Client aktif berkode `DHP-015`) dan Default User `Dewi Lestari` ber-Email `dewi.lestari+{runId}-054@qwertysystem.net`. Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Dataset Dinamis: `PT Kode Pakai Ulang {runId}-054`, `PT Email Pakai Ulang {runId}-054`.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-499: Client Code milik Client yang dihapus dipakai ulang

1. Klik `[+ New Client]`
2. Isi Company Name `PT Kode Pakai Ulang {runId}-054`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Client Code `DHP-015`, Group "Cabang Menteng"
3. Tunggu 1 detik
4. Verifikasi tidak ada pesan "Client code already exists"
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, client has been created."
7. Ketik Search `PT Kode Pakai Ulang {runId}-054`, tekan Enter
8. Klik Company Name `PT Kode Pakai Ulang {runId}-054` untuk membuka Detail
9. Verifikasi Detail menampilkan Client Code "DHP-015"
10. Klik breadcrumb "Client" untuk kembali ke List

### TC-500: Email Default User milik Client yang dihapus dipakai ulang

11. Klik `[+ New Client]`
12. Isi Company Name `PT Email Pakai Ulang {runId}-054`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Dewi Lestari dengan Email `dewi.lestari+{runId}-054@qwertysystem.net`, Group "Cabang Menteng"
13. Tunggu 1 detik
14. Verifikasi tidak ada pesan "Email already exists"
15. Klik `[Submit]`
16. Verifikasi toast sukses "Success, client has been created."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): "Tunggu 1 detik" memberi waktu debounce validasi duplikat sebelum asersi absence pesan error; Detail dan breadcrumb "Client" kembali ke List.
- Temuan untuk QA:
  - TC-499 dan TC-500 tidak menyebut kapan pesan duplikat diperiksa; spec memeriksa sesudah jeda 1 detik (debounce sekitar 500 ms pada TC-113).
