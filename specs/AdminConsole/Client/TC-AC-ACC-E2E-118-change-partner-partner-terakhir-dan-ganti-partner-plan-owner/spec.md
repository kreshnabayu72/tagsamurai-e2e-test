---
id: TC-AC-ACC-E2E-118-change-partner-partner-terakhir-dan-ganti-partner-plan-owner
title: "Change Partner oleh Principal: Remove Partner Terakhir Menjadi Direct dan Penggantian Partner Tidak Mengubah Plan Owner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-177
  - TC-AC-ACC-185
coverage:
  web: automated
---

# Change Partner oleh Principal: Remove Partner Terakhir Menjadi Direct dan Penggantian Partner Tidak Mengubah Plan Owner

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Blok kedua memakai Step ganti akun ke Partner Total Control A-14 (CV Mitra Sejati) `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, password dari `AC_CLIENT_PARTNER_TC_PASSWORD`, lalu kembali ke Total Control. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup: C-ISO-4 `PT Partner Terakhir Uji` (hanya CV Mitra Sejati; Dikonsumsi: Client menjadi Direct) dan C-01 `PT Sejahtera Abadi` (Partner CV Mitra Sejati sebagai plan owner FAMS, SAMS, SIEM; Group Area Jakarta). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang kedua Client di hook `before` dan `after` (S-06: TC-AC-ACC-185 mengubah relasi Pre-setup C-01 dan tidak menyebut pemulihan). Efek: relasi "CV Mitra Sejati" menjadi `transferred`, Managed By dan Group `PT Sejahtera Abadi` berubah, baris Changelog `Change Partner` bertambah.
- Partner pembanding Active: `CV Mitra Sejati`, `CV Mitra Lestari`. Node Group `Cabang Menteng` ada di tree Select Group.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-177: Remove Partner terakhir: Select Group wajib diisi sebelum Confirm

1. Ketik Search `PT Partner Terakhir Uji`, tekan Enter
2. Klik `[⋯]` pada baris `PT Partner Terakhir Uji` → klik `Change Partner`
3. Klik `[Remove]` pada satu-satunya Partner "CV Mitra Sejati"
4. Verifikasi field `[Group]` diganti `Select Group*` tree-picker
5. Verifikasi callout "This client has no partner and requires a group to be selected manually."
6. Verifikasi `[Confirm]` disabled sampai Group dipilih
7. Pilih Group "Cabang Menteng" pada tree `Select Group*`
8. Klik `[Confirm]`
9. Verifikasi Managed By baris `PT Partner Terakhir Uji` adalah "Direct"
10. Verifikasi Group baris `PT Partner Terakhir Uji` adalah "Cabang Menteng"

### TC-AC-ACC-185: Change Partner tidak mengubah plan owner subscription

11. Ketik Search `PT Sejahtera Abadi`, tekan Enter
12. Klik Company Name `PT Sejahtera Abadi` lalu buka Tab Subscription
13. Catat plan owner tiap subscription (FAMS, SAMS, SIEM)
14. Klik breadcrumb "Client" untuk kembali ke List
15. Ketik Search `PT Sejahtera Abadi`, tekan Enter
16. Klik `[⋯]` pada baris `PT Sejahtera Abadi` → klik `Change Partner`
17. Klik `[Remove]` pada "CV Mitra Sejati"
18. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
19. Klik `[Confirm]`
20. Tunggu aksi selesai (dialog Change Partner tertutup)
21. Klik Company Name `PT Sejahtera Abadi` lalu buka Tab Subscription
22. Verifikasi plan owner tiap subscription sama dengan yang dicatat pada langkah 13
23. Verifikasi subscription dan lisensi tidak berubah
24. Ganti akun: logout lalu login sebagai Partner Total Control A-14 (CV Mitra Sejati)
25. Ketik Search `PT Sejahtera Abadi`, tekan Enter
26. Verifikasi empty state Title "No results found" dengan Description "Try adjusting your search or filter."
27. Ganti akun: logout lalu login kembali sebagai Total Control A-01

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 14 (kembali ke List), langkah 20 ("Tunggu aksi selesai" sesudah `[Confirm]` TC-AC-ACC-185 karena langkah berikutnya berpindah surface; butir 8 bagian 8b), langkah 24 dan 27 (ganti akun, Step eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras karena memakai Client dan Search sendiri). Search pada langkah 25 menemukan baris target.
- Langkah 24 sampai 26 adalah langkah observasi yang diperlukan Expected b TC-AC-ACC-185 ("Viewer Partner lama tidak lagi melihat Client") yang tidak punya langkah di TC; empty state "No results found" adalah anchor positif absence baris (butir 2 bagian 8b). Sesi Partner A-14 adalah konteks yang diasersi, bukan pemicu.
- Post Condition TC-AC-ACC-177 (seed ulang C-ISO-4) tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-185 langkah 2 ("Change Partner: ganti ke CV Mitra Lestari") ambigu antara menambah "CV Mitra Lestari" atau mengganti "CV Mitra Sejati" dengan "CV Mitra Lestari"; spec memakai penggantian (Remove "CV Mitra Sejati" lalu tambah "CV Mitra Lestari") karena Expected b menyebut Partner lama tidak lagi melihat Client.
  - TC-AC-ACC-185 Expected b klausa kedua ("sub-tab sesuai isolasi plan owner") tidak punya nilai yang dapat diverifikasi (sub-tab mana, untuk viewer mana); tidak diasersi.
  - TC-AC-ACC-185 memutasi Pre-setup C-01 `PT Sejahtera Abadi` yang dipakai banyak TC lain dan tidak menyebut Post Condition pemulihan; relasi "CV Mitra Sejati" tidak dapat dipulihkan lewat UI (relasi lama `transferred`).
