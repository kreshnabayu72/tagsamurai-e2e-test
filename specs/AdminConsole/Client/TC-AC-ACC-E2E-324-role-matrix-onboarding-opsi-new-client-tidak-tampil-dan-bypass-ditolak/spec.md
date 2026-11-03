---
id: TC-AC-ACC-E2E-324-role-matrix-onboarding-opsi-new-client-tidak-tampil-dan-bypass-ditolak
title: "Role Matrix: Opsi + New Client Tidak Tampil untuk Active-Update + Allocation dan Active-Read + Allocation, dan Request Pembuatan Client Langsung Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-440
  - TC-AC-ACC-925
coverage:
  web: automated
---

# Role Matrix: Opsi + New Client Tidak Tampil untuk Active-Update + Allocation dan Active-Read + Allocation, dan Request Pembuatan Client Langsung Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (Role Matrix negatif; akun pertama login di hook `before` spec ini, role berikutnya lewat ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`); halaman Admin Console > Client dibuka hook `beforeEach` suite):
  - Active-Update + Allocation A-W3CRE-1 (Manage active client: Update + Read; Manage allocation: Create + Read, exact-match Area Jakarta): `activeUpdateAllocationJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_ALLOC_JAKARTA_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-440).
  - Active-Read + Allocation A-AST-7 (Manage active client: Read; Manage allocation: Create + Read, exact-match Area Jakarta): `activeReadAllocationJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_ACTIVE_READ_ALLOC_JAKARTA_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-925).
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Kemampuan teknis: klien HTTP untuk request langsung ke server tanpa melalui browser (Sesi API aktor, `suite.md`: login API untuk akun role yang sedang login, token tidak dihitung sebagai sesi web; kelas a; disediakan tim FE/BE, tanpa endpoint yang dikarang) dan Fixture BE untuk membaca daftar Client (state data). Request memakai Company Name bersuffix `PT Bypass Onboarding {runId}-324` per role; tidak ada data yang berhasil dibuat.
- Tidak butuh intercept atau jam server.

## Test Steps

### Active-Update + Allocation (TC-AC-ACC-440)

1. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih Subscription Type `New`, dan buka field Client
2. Verifikasi field Client memuat sedikitnya satu Client existing
3. Verifikasi opsi `+ New Client` tidak tampil; field Client hanya memuat Client existing
4. Kirim request pembuatan Client baru langsung ke server lewat klien HTTP (tanpa melalui browser) sebagai role ini (Company Name `PT Bypass Onboarding {runId}-324`)
5. Verifikasi request pembuatan Client baru ditolak server dengan respons 403 Forbidden
6. Verifikasi tidak ada Client `PT Bypass Onboarding {runId}-324` dibuat (dibaca lewat Fixture BE; Client `PT Sejahtera Abadi` tetap terbaca sebagai anchor)

### Active-Read + Allocation (TC-AC-ACC-925)

7. Ganti akun: logout, lalu login sebagai Active-Read + Allocation A-AST-7
8. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih mode New, dan buka field Client
9. Verifikasi field Client memuat sedikitnya satu Client existing
10. Verifikasi opsi `+ New Client` tidak tampil; field Client hanya memuat Client existing
11. Kirim request pembuatan Client baru langsung ke server lewat klien HTTP (tanpa melalui browser) sebagai role ini (Company Name `PT Bypass Onboarding B {runId}-324`)
12. Verifikasi request pembuatan Client baru ditolak server dengan respons 403 Forbidden
13. Verifikasi tidak ada Client dengan nama request tersebut dibuat (dibaca lewat Fixture BE; Client `PT Sejahtera Abadi` tetap terbaca sebagai anchor)
14. Logout, lalu login kembali sebagai Total Control (A-01)

## Notes

- K-1: TC-AC-ACC-440 dan TC-AC-ACC-925 adalah TC defense-in-depth kelas a; Expected b TC kini berupa respons `403 Forbidden` atas request langsung lewat klien HTTP, sehingga sesuai bagian 8b butir 1 spec mengasersi respons server dan state data tanpa toast.
- Asersi state data (langkah 6 dan 13: tidak ada Client yang dibuat, dibaca lewat Fixture BE) bukan butir Expected TC; ditambahkan sesuai bagian 8b butir 1 (respons server dan state data) dengan anchor Client `PT Sejahtera Abadi`.
- P-5: dua TC objek-uji ringan kelas a (request langsung tanpa harness eksternal) berada di spec visibilitas role dengan permukaan sama (form Add Subscription); jumlah tidak melebihi dua. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a).
- Temuan untuk QA
  - TC-AC-ACC-440 dan TC-AC-ACC-925: `Kirim request pembuatan Client baru langsung` tidak menyebut payload/endpoint; spec tidak mengarangnya (S-13).
