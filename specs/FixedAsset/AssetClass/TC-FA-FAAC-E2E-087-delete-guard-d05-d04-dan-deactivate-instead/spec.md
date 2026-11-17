---
id: TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead
title: "Delete Guard D-05 dan D-04: Dialog Blok Asset Class yang Pernah Diposting dan Deactivate Instead"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-216
  - TC-FA-FAAC-217
  - TC-FA-FAAC-218
  - TC-FA-FAAC-226
sourceRules: ["D-05", "F-FAAC-05.k1", "FAAC-LOGIC-12a", "§4.2f#b3", "D-04", "F-FAAC-04.k1", "D-01", "§3.3#p1"]
smoke: []
dependsOn: []
trace:
  "D-05": [4, 9]
  "F-FAAC-05.k1": 4
  "FAAC-LOGIC-12a": 6
  "§4.2f#b3": 10
  "D-04": 14
  "F-FAAC-04.k1": 16
  "D-01": 19
  "§3.3#p1": 21
anchor: [7]
coverage:
  web: automated
---

# Delete Guard D-05 dan D-04: Dialog Blok Asset Class yang Pernah Diposting dan Deactivate Instead

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode literal TC, disediakan tim FE/BE lewat fixture BE): `B-USED` "Used Fixture" Active dengan Last Posted Period Mar 2026 tanpa Asset Name; `B-USEDN` "Used With Names" dengan Last Posted Period Mar 2026 dan 3 Asset Name; `B-USEDI` Inactive dengan Last Posted Period Mar 2026. Spec ini hanya membuka dialog dan membatalkannya, tidak mengubah data.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nama itu. Seed idempotent dan pemulihan dilakukan fixture BE di hook `before` dan `after`. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-216: Delete Asset Class yang pernah diposting (Guard 1) menampilkan D-05

1. Ketik Search `B-USED`, tekan Enter
2. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
3. Klik ikon `⋯` pada baris `B-USED`, lalu pilih `Delete`
4. Verifikasi Dialog Blok `Cannot Delete Asset Class` berisi `• B-USED – Used Fixture` dan `This asset class was used in depreciation for Mar 2026.` dengan tombol `Cancel` dan `Deactivate instead` (Enabled)
5. Klik `Cancel`
6. Verifikasi baris `B-USED` masih ada di tabel (Asset Class tidak terhapus)
7. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-226: Deactivate instead Hidden pada D-05 bila Asset Class sudah Inactive

8. Klik ikon `⋯` pada baris `B-USEDI`, lalu pilih `Delete`
9. Verifikasi Dialog Blok D-05 `Cannot Delete Asset Class` tampil dengan tombol `Cancel`
10. Verifikasi tombol `Deactivate instead` tidak tampil
11. Klik `Cancel`

### TC-FA-FAAC-218: Deactivate instead pada D-05 menampilkan D-04 bila masih ada Asset Name

12. Klik ikon `⋯` pada baris `B-USEDN`, lalu pilih `Delete`
13. Klik `Deactivate instead`
14. Verifikasi Dialog Blok `Cannot Deactivate Asset Class` berisi `• B-USEDN – Used With Names` dan `This asset class has 3 asset names. Move them to another asset class first.` dengan tombol `OK`
15. Klik `OK`
16. Verifikasi toggle Active pada baris `B-USEDN` tetap On

### TC-FA-FAAC-217: Deactivate instead pada D-05 membuka konfirmasi Deactivate bila tanpa Asset Name

17. Klik ikon `⋯` pada baris `B-USED`, lalu pilih `Delete`
18. Klik `Deactivate instead`
19. Verifikasi Dialog `Deactivate Asset Class` (D-01) berisi `• B-USED – Used Fixture` dan `Are you sure you want to deactivate it?` dengan tombol `Cancel` dan `Deactivate`
20. Klik `Cancel`
21. Verifikasi tidak ada perubahan: toggle Active pada baris `B-USED` tetap On (Asset Class tetap Active)
22. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: TC-216 dan TC-226 (dialog D-05 saja) lebih dulu, lalu TC-218 dan TC-217 yang melanjutkan ke dialog Deactivate; semua batal sehingga tidak ada data berubah.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 2 (baseline Changelog, S-12), langkah 5, 11, 15, dan 20 (menutup dialog), serta langkah 22 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal (`B-USED`, `B-USEDN`, `B-USEDI`) dan asersi bergantung pada nama dan jumlah Asset Name; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Aksi hanya membuka dialog lalu membatalkan sehingga data tidak berubah.
4. S-05 dan P-1: Expected "tanpa log" pada TC-216 diasersi di spec ini (langkah 7) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Temuan untuk QA: Tabel Data Uji Pre-setup TC hanya memuat akun fixture; data seed Asset Class (`B-USED`, `B-USEDN`, `B-USEDI`) hanya tertulis di Precondition tiap TC dan disediakan tim FE/BE (S-11).
