---
id: TC-AC-SG-E2E-041-delete-group-konfirmasi-hapus-subtree-pelepasan-group-role-manager-dan-klik-ganda
title: "Delete Group: Konfirmasi Menghapus Subtree, Pelepasan Group Role dan Group Manager, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-133
  - TC-AC-SG-146
  - TC-AC-SG-148
coverage:
  web: automated
---

# Delete Group: Konfirmasi Menghapus Subtree, Pelepasan Group Role dan Group Manager, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Hapus Utama (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`), nama literal karena TC mengasersi penugasan user Pre-setup pada node bernama:
  - `Hapus Warn A`: tanpa entitas, Group Role `Manage partner` pada `Joko Susilo`.
  - `Hapus Warn B`: tanpa entitas, Group Role pada `Nina Amelia`; anak `Hapus Warn B1` (Group Manager `Lia Marlina`) dan `Hapus Warn B2`.
- Spec ini menghapus node Pre-setup `Hapus Warn A` dan subtree `Hapus Warn B` (penugasan user Pre-setup tidak dapat dimiliki spec, S-06 pengecualian 2026-10-30). Pemulihan lewat Fixture BE di hook `before` dan `after` serta di langkah 9 (antar blok TC-133 dan TC-146). Efek: Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) entitas bertambah oleh penghapusan dan pemulihan dan tidak diasersi.
- Akun yang dibuka di Settings > User dan Settings > Role & Permission adalah akun aktor yang sama (akses modul terkait, Pre-setup #40).
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas dan pembacaan penugasan Group Role/Manager untuk Expected TC-133 butir c), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-133: Konfirmasi Delete menghapus node dan seluruh subtree

1. Ketik Search `Hapus Warn B`, tekan Enter
2. Klik ikon `⋯` pada baris `Hapus Warn B`, lalu pilih "Delete"
3. Klik `[Delete]` pada dialog
4. Verifikasi toast sukses: "Success, group has been deleted."
5. Verifikasi `Hapus Warn B`, `Hapus Warn B1`, dan `Hapus Warn B2` hilang dari tabel (cascade tanpa opsi include/exclude)
6. Verifikasi `Hapus Warn B`, `Hapus Warn B1`, dan `Hapus Warn B2` hilang dari sidebar
7. Verifikasi penugasan Group Role `Nina Amelia` pada node terhapus dilepas
8. Verifikasi penugasan Group Manager `Lia Marlina` pada node terhapus dilepas
9. Lewat Fixture BE, pulihkan subtree `Hapus Warn B` beserta penugasan Group Role `Nina Amelia` dan Group Manager `Lia Marlina` hingga tersimpan
10. Muat ulang halaman (F5)

### TC-AC-SG-148: Klik Delete ganda tidak memicu penghapusan ganda

11. Ketik Search `Hapus Warn A`, tekan Enter
12. Klik ikon `⋯` pada baris `Hapus Warn A`, lalu pilih "Delete"
13. Klik `[Delete]` dua kali berturut-turut
14. Verifikasi toast sukses "Success, group has been deleted." tampil sekali
15. Verifikasi toast "This group is no longer available." tidak tampil

### TC-AC-SG-146: Delete melepas Group Role dan Group Manager tanpa pengalihan otomatis

16. Ganti isi kotak search dengan `Hapus Warn B`, tekan Enter
17. Klik ikon `⋯` pada baris `Hapus Warn B`, lalu pilih "Delete"
18. Klik `[Delete]`
19. Tunggu aksi selesai (dialog tertutup dan baris `Hapus Warn B` hilang dari tabel)
20. Buka Settings > User lewat sidebar
21. Buka Detail `Nina Amelia`, lalu buka Tab Role
22. Verifikasi Tab Role pada Detail `Nina Amelia` termuat dan tampil
23. Verifikasi penugasan Group Role `Nina Amelia` pada `Hapus Warn B` hilang dan tidak dialihkan ke group lain (Tab Role tidak memuat penugasan Group Role)
24. Buka Settings > Role & Permission lewat sidebar, lalu buka Tab Group Manager List
25. Verifikasi Tab Group Manager List termuat dan tampil
26. Verifikasi penugasan Group Manager `Lia Marlina` untuk `Hapus Warn B1` hilang dari Tab Group Manager List

## Notes

- Langkah penghubung (S-03): langkah 1, 11, dan 16 (Search untuk menemukan baris target, R-16); langkah 9 dan 10 (pemulihan baseline dan muat ulang antar blok, S-09); langkah 19 (tunggu aksi selesai, bagian 8b butir 8) dan langkah 20 serta 24 (navigasi modul lain); langkah 13 dihitung satu aksi klik ganda.
- Perubahan urutan TC (S-10): TC-148 ditempatkan sebelum TC-146 karena TC-146 meninggalkan Settings > Group dan menjadi blok terakhir; TC-133 berada paling awal agar pemulihan subtree `Hapus Warn B` dilakukan sebelum TC-146 memakainya lagi.
- Langkah 22 dan 25 (asersi tambahan, 8b.2): `Verifikasi` Tab Role dan Tab Group Manager List termuat dan tampil, sebagai anchor positif sebelum `Verifikasi` absence di langkah 23 dan 26; Expected TC-AC-SG-146 tidak memuat klausa anchor ini.
- TC-AC-SG-144 dan TC-AC-SG-145 (fallback seleksi ke All Groups sesudah Delete) berada di spec 110. TC-AC-SG-134 berada di spec absence 091.
- Temuan untuk QA:
  - TC-AC-SG-133 butir c (penugasan dilepas) tidak memberi langkah observasi; spec mengasersinya lewat kemampuan baca Fixture BE (disediakan tim FE/BE, tanpa endpoint karangan).
  - TC-AC-SG-146 Expected a "tidak dialihkan ke group lain" tidak menyebut kondisi Tab Role setelah Delete; spec mengasersi Tab Role tidak memuat penugasan Group Role bagi `Nina Amelia`, dengan asumsi Pre-setup #18 hanya memberinya satu penugasan pada `Hapus Warn B`.
  - Email akun `Joko Susilo`, `Nina Amelia`, dan `Lia Marlina` tidak tertulis di Pre-setup (hanya nama tampil); jenis Group Role `Nina Amelia` pada `Hapus Warn B` tidak disebut.
  - TC-AC-SG-148 tidak menyebut cara cek bahwa hanya satu penghapusan terjadi; spec mengasersi toast sukses tepat satu kali dan tidak adanya toast "This group is no longer available."
