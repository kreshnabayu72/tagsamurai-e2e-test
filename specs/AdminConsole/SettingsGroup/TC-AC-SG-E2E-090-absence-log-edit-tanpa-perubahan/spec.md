---
id: TC-AC-SG-E2E-090-absence-log-edit-tanpa-perubahan
title: "Absence Log Edit Group Tanpa Perubahan di Changelog, Activity Log, dan System Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-125
  - TC-AC-SG-328
coverage:
  web: automated
---

# Absence Log Edit Group Tanpa Perubahan di Changelog, Activity Log, dan System Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Activity Log Admin Console dan ke Settings > User > Detail akun aktor > Tab System Log tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus hook `after`): `Region B {runId}-090` (level 1, tanpa entitas). Node ini tidak berubah oleh spec; Pohon Uji Utama (Pre-setup #16) tidak disentuh.
- Baseline audit trail permanen dicatat per TC sebelum aksi pemicu TC itu: TC-AC-SG-125 mencatat jumlah entri Changelog untuk Group Name `Region B {runId}-090`; TC-AC-SG-328 mencatat jumlah total entri Changelog Group, jumlah entri Activity Log (saringan Object `Group`), dan jumlah entri System Log aktor. Kemampuan baca jumlah entri disediakan tim FE/BE.
- Kemampuan mengamati status respons permintaan yang dipicu `[Save]` (untuk `204 No Content`) disediakan tim FE.
- Jendela tunggu 5 detik sebelum membaca surface log adalah pilihan spec (bukan nilai TC atau PRD), karena pencatatan bersifat eventual dan TC tidak menyatakan durasinya.
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).

## Test Steps

### Baseline sebelum aksi

1. Klik ikon Changelog pada toolbar
2. Catat jumlah entri untuk Group Name `Region B {runId}-090` pada Modal "Changelog: Group" sebagai baseline Changelog TC-AC-SG-125
3. Tutup Modal Changelog dengan `✕`
4. Buka halaman Settings > Group lewat sidebar
5. Ketik Search `{runId}-090`, tekan Enter
6. Catat Modified By dan Last Updated baris `Region B {runId}-090`

### TC-AC-SG-125: Edit tanpa perubahan menampilkan toast netral dan tidak mencatat log

7. Klik ikon `⋯` pada baris `Region B {runId}-090` lalu `Edit`
8. Klik `[Save]` tanpa mengubah nilai
9. Verifikasi toast netral (Info): "No changes to save."
10. Verifikasi respons server atas `[Save]` adalah `204 No Content`
11. Verifikasi popup Edit Group tertutup
12. Verifikasi Modified By dan Last Updated baris `Region B {runId}-090` sama dengan nilai yang dicatat
13. Tunggu toast lama hilang otomatis
14. Klik ikon `⋯` pada baris `Region B {runId}-090` lalu `Edit`
15. Ketik `  Region B {runId}-090  ` (hanya spasi di tepi) pada field nama, lalu klik `[Save]`
16. Verifikasi toast netral (Info): "No changes to save."
17. Verifikasi respons server atas `[Save]` adalah `204 No Content`
18. Verifikasi popup Edit Group tertutup
19. Verifikasi Modified By dan Last Updated baris `Region B {runId}-090` sama dengan nilai yang dicatat
20. Tunggu 5 detik
21. Klik ikon Changelog pada toolbar dan baca entri terbaru
22. Verifikasi jumlah entri untuk Group Name `Region B {runId}-090` bertambah 0 dari baseline Changelog TC-AC-SG-125 (tidak ada entri baru untuk `Region B {runId}-090`)
23. Tutup Modal Changelog dengan `✕`

### TC-AC-SG-328: Edit tanpa perubahan tidak menulis entri ke surface log mana pun

24. Klik ikon Changelog pada toolbar
25. Catat jumlah total entri Modal "Changelog: Group" sebagai baseline Changelog TC-AC-SG-328
26. Tutup Modal Changelog dengan `✕`
27. Buka Activity Log Admin Console dan saring Object `Group`
28. Catat jumlah entri sebagai baseline Activity Log TC-AC-SG-328
29. Buka Settings > User > Detail akun aktor > Tab System Log
30. Catat jumlah entri sebagai baseline System Log TC-AC-SG-328
31. Buka halaman Settings > Group lewat sidebar
32. Ketik Search `{runId}-090`, tekan Enter
33. Tunggu toast lama hilang otomatis
34. Klik ikon `⋯` pada baris `Region B {runId}-090` lalu `Edit`
35. Klik `[Save]` tanpa perubahan
36. Verifikasi toast netral: "No changes to save."
37. Tunggu 5 detik
38. Klik ikon Changelog pada toolbar
39. Verifikasi jumlah total entri Modal "Changelog: Group" bertambah 0 dari baseline Changelog TC-AC-SG-328
40. Tutup Modal Changelog dengan `✕`
41. Buka Activity Log Admin Console dan saring Object `Group`
42. Verifikasi jumlah entri Activity Log bertambah 0 dari baseline Activity Log TC-AC-SG-328
43. Buka Settings > User > Detail akun aktor > Tab System Log
44. Verifikasi jumlah entri System Log aktor bertambah 0 dari baseline System Log TC-AC-SG-328

## Notes

- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 1 sampai 6 dan 24 sampai 32 (baseline per TC sebelum aksi pemicu, membuka kembali Settings > Group, Search `{runId}-090` untuk menemukan baris target, mencatat nilai), langkah 13 dan 33 (menunggu toast lama hilang sebelum toast berikutnya diasersi, R-12), langkah 20 dan 37 (jendela tunggu 5 detik), dan penutupan Modal Changelog.
- Kelas g (absence). Anchor positif tiap asersi absence: toast netral "No changes to save." yang diasersi segera setelah `[Save]` (respons server sudah diproses) dan jumlah baseline pada surface yang sama (surface agregat); dengan seed `Region B {runId}-090` yang tidak menyentuh entitas lain, baseline total dipakai karena pemicu tidak menghasilkan entri yang bisa dijadikan anchor (bagian 8b butir 2).
- S-05: TC-AC-SG-125 terbelah antara presence (toast netral, popup tertutup, Modified By dan Last Updated tidak berubah) dan absence (nol entri Changelog); keduanya ditulis di spec ini dengan aksi nyata dan baseline sendiri. TC-AC-SG-328 ditulis di spec ini dengan aksi nyata. Rujukan dari spec 087 (pencatatan Create dan Edit) hanya berupa catatan di `## Notes` spec itu.
- TC-AC-SG-125 dan TC-AC-SG-328 menarget node Pre-setup `Region B`; spec memakai node milik spec `Region B {runId}-090` (S-06). Kedua TC tidak mengubah node, sehingga satu node dipakai bergantian tanpa langkah pemulihan.
- Temuan untuk QA:
  - TC-AC-SG-125 Expected butir b menulis "(0 entri)" untuk `Region B`; spec mengasersi jumlah entri sama dengan baseline karena seed mungkin menulis entri awal.
  - TC-AC-SG-328 tidak menyebut cara menghitung "tidak menambah entri apa pun" pada Activity Log dan System Log yang tumbuh; spec memakai selisih terhadap baseline yang dicatat sebelum aksi.
  - TC-AC-SG-125 langkah 4 menulis ketikan `"  Region B  "` dengan spasi tepi; spec menambah suffix `{runId}-090` pada nama dan mempertahankan spasi di tepi.
- Alasan di atas sekitar 35 langkah: seluruh langkah satu topik (absence log Edit tanpa perubahan) dan satu harness: tiap blok TC mencatat baseline sendiri pada surface log yang diasersinya sebelum aksi pemicu blok itu (S-12), lalu membandingkannya dengan selisih +0; membaca log berulang pada surface yang sama tidak dapat dipecah tanpa mengulang baseline.
