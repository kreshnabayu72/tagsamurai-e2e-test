---
id: TC-AC-SU-E2E-050-sub-tab-global-role-aktor-read-only
title: "Sub-tab Global Role: Aktor Read Only Melihat Kontrol Disabled"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-189
coverage:
  web: automated
---

# Sub-tab Global Role: Aktor Read Only Melihat Kontrol Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only, `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-050` tanpa tingkat akses dan bukan Group Manager; `Manage group` ON.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-050@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-050`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-050` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-189: Aktor Read Only membuka Sub-tab Global Role

1. Ketik Search `Budi Santoso {runId}-050`, tekan Enter
2. Klik nama `Budi Santoso {runId}-050` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Verifikasi Tab Role tampil
4. Verifikasi Sub-tab Global Role tampil
5. Hover switch baris `Manage group`
6. Hover checkbox C baris `Manage group`
7. Verifikasi switch dan CRUD Global Role tampil namun disabled
8. Verifikasi tooltip `"Read Only access cannot modify data."`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Baris yang dihover dipilih `Manage group` (aktif) untuk TC yang menulis "sebuah baris aktif".
