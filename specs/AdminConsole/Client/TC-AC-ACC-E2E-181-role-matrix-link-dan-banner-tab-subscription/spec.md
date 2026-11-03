---
id: TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription
title: "Role Matrix: Link dan Banner Tab Subscription per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-610
  - TC-AC-ACC-611
  - TC-AC-ACC-612
  - TC-AC-ACC-613
coverage:
  web: automated
---

# Role Matrix: Link dan Banner Tab Subscription per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Active-Read-Allocation-Read (Manage active client: Read; Manage allocation: Read; exact-match Area Jakarta), A-ROL-9 | `activeReadAllocationReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_READ_ALLOC_READ_PASSWORD` |
| Group Manager (Principal, scope Area Jakarta + descendant), A-03 | `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GM_PASSWORD` |
| Default User (Principal), A-ROL-3 | `defaultUserPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_DU_PRINCIPAL_PASSWORD` |
| Archived-Read (Manage archived client: Read, exact-match Area Jakarta), A-08 | `archivedReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_READ_PASSWORD` |

- Env var `AC_CLIENT_ACTIVE_READ_ALLOC_READ_PASSWORD`, `AC_CLIENT_GM_PASSWORD`, `AC_CLIENT_DU_PRINCIPAL_PASSWORD`, `AC_CLIENT_ARCHIVED_READ_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Tabel "Role yang diuji" di atas; blok dijalankan berurutan per akun dengan Step ganti akun eksplisit. Login akun aktor pertama (Active-Read-Allocation-Read, A-ROL-9) di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): "PT Sejahtera Abadi" (C-01, Active) dan "PT Karya Abadi" (C-04, Archived). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### Active-Read-Allocation-Read: TC-AC-ACC-610

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`
4. Verifikasi info banner tampil di atas toolbar tab: "This tab is read-only. To add, renew, or cancel a subscription, use Manage in Client Subscription."
5. Verifikasi link `[Manage in Client Subscription →]` tampil di toolbar tab

### Group Manager (Principal, scope Area Jakarta + descendant): TC-AC-ACC-611

6. Logout dari akun Active-Read-Allocation-Read
7. Login sebagai Group Manager (Principal, scope Area Jakarta + seluruh descendant)
8. Ketik Search `PT Sejahtera Abadi`, tekan Enter
9. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
10. Klik Tab `Subscription`
11. Verifikasi info banner tampil di atas toolbar tab: "This tab is read-only. To add, renew, or cancel a subscription, use Manage in Client Subscription."
12. Verifikasi link `[Manage in Client Subscription →]` tampil di toolbar tab

### Default User (Principal): TC-AC-ACC-612

13. Logout dari akun Group Manager
14. Login sebagai Default User (Principal)
15. Ketik Search `PT Sejahtera Abadi`, tekan Enter
16. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
17. Klik Tab `Subscription`
18. Verifikasi info banner tampil di atas toolbar tab: "This tab is read-only. To add, renew, or cancel a subscription, use Manage in Client Subscription."
19. Verifikasi link `[Manage in Client Subscription →]` tampil di toolbar tab

### Archived-Read (Manage archived client: Read): TC-AC-ACC-613

20. Logout dari akun Default User (Principal)
21. Login sebagai Archived-Read (Manage archived client: Read, exact-match Area Jakarta)
22. Klik sub-tab `Archived`, ketik Search `PT Karya Abadi`, tekan Enter
23. Klik Company Name "PT Karya Abadi" untuk membuka Detail
24. Klik Tab `Subscription`
25. Verifikasi toolbar Tab `Subscription` memuat `[Download]` dan `[Changelog]`
26. Verifikasi link `[Manage in Client Subscription →]` dan info banner tidak tampil
27. Klik Tab `Asset Control`
28. Verifikasi Tab `Asset Control` menampilkan ikon Changelog

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec ditulis per blok role (bukan perulangan identik) karena role pada TC-613 menguji polaritas berbeda (link dan banner tidak tampil) dan Client yang dibuka berbeda; ganti akun memakai Step eksplisit (bagian 3a). Anchor absence TC-613: Verifikasi `[Download]` dan `[Changelog]` pada toolbar yang sama mendahului asersi link dan banner tidak tampil.
- Temuan untuk QA (S-15): TC-610/611/612 tidak menyebut sub-tab asal "PT Sejahtera Abadi" (spec memakai Active); TC-613 Precondition menyebut Detail "PT Karya Abadi" (C-04, Archived) sehingga spec memakai sub-tab `Archived`. TC-610 memakai aktor A-ROL-9 yang tercantum di Tabel A3, TC-612 memakai A-ROL-3; kedua password env var baru perlu didaftarkan tim FE. Post Condition seluruh TC `-`.
