---
id: TC-AC-SG-E2E-028-create-subgroup-parent-pemilik-aksi-elipsis-sidebar-dan-level-satu-saat-node-lain-terpilih
title: "Create Subgroup: Parent Pemilik Aksi, Elipsis Sidebar, dan Level 1 saat Node Lain Terpilih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-91
  - TC-AC-SG-92
  - TC-AC-SG-93
coverage:
  web: automated
---

# Create Subgroup: Parent Pemilik Aksi, Elipsis Sidebar, dan Level 1 saat Node Lain Terpilih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data seed milik spec (entitas Principal, di-seed Fixture BE di hook `before`): `Region A-{runId}-028` (level 1) dengan anak `Branch 2-{runId}-028`; `Head Office-{runId}-028` (level 1). Nama TC `Region A`, `Branch 2`, dan `Head Office` diganti nama bersuffix milik spec karena target aksi tulis tidak memakai node Pre-setup bersama (S-06).
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec |
|---|---|---|
| TC-AC-SG-91 | `Floor Baru` (anak `Branch 2`) | `Floor Baru-{runId}-028` |
| TC-AC-SG-92 | `Legal Dept` (anak `Head Office`) | `Legal Dept-{runId}-028` |
| TC-AC-SG-93 | `Region Level Satu` (level 1) | `Region Level Satu-{runId}-028` |

- Kemampuan teknis: Fixture BE (seeding dan penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-91: Add Subgroup dari row action tabel

1. Ketik Search `Branch 2-{runId}-028`, tekan Enter
2. Klik ikon `⋯` pada baris `Branch 2-{runId}-028`, lalu pilih "+ Add Subgroup"
3. Ketik `Floor Baru-{runId}-028` pada Group Name, klik `[Submit]`
4. Verifikasi toast sukses: "Success, group has been created."
5. Verifikasi popup tertutup
6. Verifikasi `Floor Baru-{runId}-028` muncul di sidebar sebagai anak `Branch 2-{runId}-028`
7. Ganti isi kotak search dengan `Floor Baru-{runId}-028`, tekan Enter
8. Hover nama group pada baris `Floor Baru-{runId}-028`
9. Verifikasi full path pada hover tabel: "Region A-{runId}-028 > Branch 2-{runId}-028 > Floor Baru-{runId}-028"
10. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-92: Add Subgroup dari elipsis sidebar

11. Klik ikon `⋯` pada node `Head Office-{runId}-028` di sidebar, lalu pilih "+ Add Subgroup"
12. Verifikasi popup menampilkan "Under: Head Office-{runId}-028"
13. Ketik `Legal Dept-{runId}-028` pada Group Name, klik `[Submit]`
14. Verifikasi subgroup `Legal Dept-{runId}-028` dibuat di bawah `Head Office-{runId}-028` di sidebar
15. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-93: `[+] Group` selalu membuat level 1

16. Klik node `Region A-{runId}-028` di sidebar
17. Klik `[+] Group` di Sidebar Group Tree
18. Verifikasi Popup New Group tanpa "Under:"
19. Ketik `Region Level Satu-{runId}-028` pada Group Name, klik `[Submit]`
20. Verifikasi group `Region Level Satu-{runId}-028` dibuat sebagai level 1 di sidebar (sibling `Region A-{runId}-028`, bukan anak)
21. Verifikasi baris `Branch 2-{runId}-028` tampil pada tabel node `Region A-{runId}-028`
22. Verifikasi `Region Level Satu-{runId}-028` tidak tampil pada tabel node `Region A-{runId}-028`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 7 (Search untuk menemukan baris target, R-16), langkah 10 (reset Search, S-09).
- Langkah 21 adalah anchor positif bagi asersi absence langkah 22 pada permukaan tabel yang sama (bagian 8b butir 2).
- TC-AC-SG-93 tidak menyebut toast pada Expected; Submit sukses diamati lewat langkah 20.
