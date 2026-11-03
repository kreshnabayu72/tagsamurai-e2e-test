---
id: TC-AC-ACC-E2E-152-delete-archived-diblok-trial-active-d03
title: "Delete Client Archived dengan Trial Active Diblok D-03 Seperti Term Paid Active"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1020
coverage:
  web: automated
---

# Delete Client Archived dengan Trial Active Diblok D-03 Seperti Term Paid Active

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data (Tabel A3, kelas Residen; hanya dibaca karena Delete diblok): C-FX17-4 `PT Arsip Trial Aktif` (Archived; FAMS Archive; SAMS Trial Active). Spec ini terpisah dari spec Delete lain karena kondisi data blok (Trial Active) butuh fixture khusus (prinsip 12).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-1020: Delete Client Archived dengan Trial Active diblok D-03 seperti term paid Active

1. Klik sub-tab Archived, ketik Search `PT Arsip Trial Aktif`, tekan Enter
2. Klik `[⋯]` pada baris `PT Arsip Trial Aktif` → klik `Delete`, lalu ketik nama persis `PT Arsip Trial Aktif` dan centang "I understand this action cannot be undone"
3. Klik `[Delete]`
4. Verifikasi dialog blok Title "Cannot Delete Client" dengan bullet `• PT Arsip Trial Aktif`
5. Verifikasi dialog blok memuat "This client still has active or expiring subscriptions. Cancel all subscriptions before deleting."
6. Verifikasi dialog blok memuat tombol `[OK]`
7. Klik `[OK]`
8. Ganti isi Search dengan `PT Arsip Trial Aktif`, tekan Enter
9. Verifikasi baris `PT Arsip Trial Aktif` tetap tampil di sub-tab Archived (Client tidak terhapus)

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (tanpa awalan Verifikasi): klik `[OK]` penutup dialog blok (langkah 7) dan Search ulang (langkah 8). Langkah 2 menyalin Langkah 2 TC (buka Delete, ketik nama, centang checkbox).
- Post Condition TC-AC-ACC-1020: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-1020 Expected b ("Client tidak terhapus") ditulis sebagai baris yang tetap tampil di sub-tab Archived; TC tidak menyebut cara observasi lain.
