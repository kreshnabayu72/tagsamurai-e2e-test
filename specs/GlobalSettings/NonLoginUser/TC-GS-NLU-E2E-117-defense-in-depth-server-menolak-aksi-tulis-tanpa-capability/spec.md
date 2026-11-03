---
id: TC-GS-NLU-E2E-117-defense-in-depth-server-menolak-aksi-tulis-tanpa-capability
title: "Defense-in-depth: server menolak aksi tulis tanpa capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-431
  - TC-GS-NLU-432
  - TC-GS-NLU-433
  - TC-GS-NLU-434
  - TC-GS-NLU-435
  - TC-GS-NLU-436
coverage:
  web: automated
---

# Defense-in-depth: server menolak aksi tulis tanpa capability

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; request dikirim langsung ke server lewat sesi API aktor tanpa melewati browser, dan state data dibaca lewat fixture BE. Tidak ada respons yang di-mock atau di-intercept.
- Role yang diuji (akun Pre-setup TC; password hanya lewat `Spectra.env`):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-NLU-431, 432 | Read Only | Yudi Pratomo | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 2) | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-NLU-433 | Manage user and role (Update-Only: R+U) | Bayu Saputra | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 5) | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-NLU-434 | Manage user and role (Delete-Only: R+D) | Citra Melati | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` (No. 6) | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-NLU-435 | Manage user and role (Create-Only: C+R) | Lestari Ayu | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` (No. 4) | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-NLU-436 | Basic (Access Global Settings, tanpa tier dan tanpa role Manage user and role) | Gita Permata | `basicGlobalSettings_automated_{namaCompany}@qwertysystem.net` (No. 8) | `Spectra.env.GS_BASIC_PASSWORD` |

- Environment variable: `GS_RO_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_BASIC_PASSWORD`.
- Login akun aktor pertama (Read Only) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah eksplisit membuka sesi API aktor berikutnya; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web (lihat `suite.md`, bagian Hook suite); kemampuan disediakan tim BE/FE.
- Kemampuan teknis: klien HTTP untuk request langsung ke server, pembacaan status respons, dan fixture BE untuk membaca state data Non-Login User (disediakan tim FE/BE).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Division `Operations`, Represented By `Ahmad Fauzi`, Active):
  - `Target Edit {runId}-117` (First Name `Target`, Last Name `Edit {runId}-117`), `Target Hapus {runId}-117`, `Target Status {runId}-117`, `Target Convert {runId}-117`, Email `<nama>+{runId}-117@qwertysystem.net`.
  - Payload Create yang ditolak: First Name `Tolak`, Last Name `Buat Satu {runId}-117` (TC-GS-NLU-431) dan `Buat Dua {runId}-117` (TC-GS-NLU-436), Division `Logistics`, Email `tolak<n>+{runId}-117@qwertysystem.net`, Represented By `Ahmad Fauzi`.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-117` yang tersisa tanpa mengasumsikan seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-431: Server menolak Create oleh Read Only walau UI di-bypass

1. Buka sesi API aktor Read Only (Yudi Pratomo, `Spectra.env.GS_RO_PASSWORD`)
2. Kirim request membuat Non-Login User `Tolak Buat Satu {runId}-117` langsung lewat sesi API aktor tanpa melalui UI
3. Verifikasi server menolak dengan `403 Forbidden`
4. Verifikasi lewat fixture BE bahwa Non-Login User `Tolak Buat Satu {runId}-117` tidak ada (data tidak berubah)

### TC-GS-NLU-432: Server menolak Edit oleh Read Only walau UI di-bypass

5. Kirim request mengubah First Name `Target Edit {runId}-117` menjadi `Diubah` langsung lewat sesi API aktor Read Only
6. Verifikasi server menolak dengan `403 Forbidden`
7. Verifikasi lewat fixture BE bahwa First Name `Target Edit {runId}-117` tetap `Target` (data tidak berubah)

### TC-GS-NLU-433: Server menolak Delete oleh Update-Only walau UI di-bypass

8. Ganti akun: buka sesi API aktor Manage user and role (Update-Only: R+U) (Bayu Saputra, `Spectra.env.GS_UPDATE_PASSWORD`)
9. Kirim request menghapus `Target Hapus {runId}-117` langsung lewat sesi API aktor tanpa melalui UI
10. Verifikasi server menolak dengan `403 Forbidden`
11. Verifikasi lewat fixture BE bahwa `Target Hapus {runId}-117` masih ada (data tidak berubah)

### TC-GS-NLU-434: Server menolak Activate/Deactivate oleh Delete-Only walau UI di-bypass

12. Ganti akun: buka sesi API aktor Manage user and role (Delete-Only: R+D) (Citra Melati, `Spectra.env.GS_DELETE_PASSWORD`)
13. Kirim request mengubah status `Target Status {runId}-117` menjadi Inactive langsung lewat sesi API aktor tanpa melalui UI
14. Verifikasi server menolak dengan `403 Forbidden`
15. Verifikasi lewat fixture BE bahwa status `Target Status {runId}-117` tetap Active (data tidak berubah)

### TC-GS-NLU-435: Server menolak Convert oleh Create-Only walau UI di-bypass

16. Ganti akun: buka sesi API aktor Manage user and role (Create-Only: C+R) (Lestari Ayu, `Spectra.env.GS_CREATE_PASSWORD`)
17. Kirim request mengonversi `Target Convert {runId}-117` menjadi Login User langsung lewat sesi API aktor tanpa melalui UI
18. Verifikasi server menolak dengan `403 Forbidden`
19. Verifikasi lewat fixture BE bahwa `Target Convert {runId}-117` tetap bertipe Non-Login User (data tidak berubah)

### TC-GS-NLU-436: Server menolak aksi tulis oleh aktor tanpa akses sama sekali

20. Ganti akun: buka sesi API aktor Basic (Gita Permata, `Spectra.env.GS_BASIC_PASSWORD`)
21. Kirim request Create Non-Login User `Tolak Buat Dua {runId}-117` langsung lewat sesi API aktor tanpa UI
22. Verifikasi server menolak dengan `403 Forbidden`
23. Verifikasi lewat fixture BE bahwa Non-Login User `Tolak Buat Dua {runId}-117` tidak ada (tidak ada record dibuat)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-GS-NLU-431 sampai 436 adalah TC kelas a (defense-in-depth) yang Expected-nya berupa respons API; tetap masuk spec FE+BE sebagai TC granular sumber (satu TC tepat satu spec), walau isinya tumpang tindih dengan `tc-non-login-user-backend.md`.
- Langkah penghubung (S-03): langkah 1, 8, 12, 16, 20 (ganti akun dengan membuka sesi API aktor berikutnya, S-07).
- Request langsung ke server (bagian 8b butir 1): asersi hanya status respons dan state data lewat fixture BE; Expected b TC-GS-NLU-431 sampai 435 (toast error `You don't have permission to do this.` dan elemen tak berhak disembunyikan) adalah perilaku FE dan tidak disalin ke spec ini (lihat Temuan untuk QA). Langkah TC "Muat ulang list" hanya melayani Expected b itu sehingga tidak ditulis.
- Pelaku sesi UI: hook `before` login UI sebagai Read Only (akun aktor pertama, S-07) dan tidak dipakai langkah; seluruh request lewat sesi API aktor.
- Alasan jumlah langkah: nominal 23 langkah, semua blok satu kelas harness (kelas a), tiap blok memakai akun dan record sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-431 sampai 435 Expected b menyebut toast error `You don't have permission to do this.` dan elemen disembunyikan sesudah request langsung; perilaku FE tidak dapat dihasilkan oleh request langsung (bagian 8b butir 1), sehingga perlu TC FE terpisah bila diinginkan.
  - Email akun Create-Only, Update-Only, dan Delete-Only pada Pre-setup TC (`manageUser{Create,Update,Delete}_automated_{namaCompany}`) berbeda dari komentar `.env.example` untuk `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD` (`createOnly_`, `updateOnly_`, `deleteOnly_...qaTeam1`); kecocokan akun dan nama env perlu dikonfirmasi tim FE.
  - TC-GS-NLU-431 sampai 436 tidak menyebut payload request; spec memakai payload valid milik spec.
