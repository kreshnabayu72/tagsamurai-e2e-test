---
id: TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss
title: "Guided Tooltip Tab Position: Muncul Otomatis pada Kunjungan Pertama, Done, Skip, dan Klik Overlay Menandai Seen, serta Replay lewat Tombol [?]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-16
  - TC-GS-POS-18
  - TC-GS-POS-19
  - TC-GS-POS-20
  - TC-GS-POS-21
coverage:
  web: automated
---

# Guided Tooltip Tab Position: Muncul Otomatis pada Kunjungan Pertama, Done, Skip, dan Klik Overlay Menandai Seen, serta Replay lewat Tombol [?]

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: kunjungan ke tab Position adalah pemicu auto-open Guided Tooltip dan kunjungan ulang (klik sub-tab User List lalu Position) adalah aksi yang diuji, sehingga langkah buka ditulis di `## Test Steps` dan bukan di hook `beforeEach`.
- Data: tidak ada Data Pre-setup dan tidak ada Data Dinamis yang dipakai langkah.
- Guided Tooltip (page_key `gs-position`): spec ini menguji flag `guided_tooltip_seen_gs-position` sendiri, sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`). Hook `before` mencatat nilai awal flag akun Total Control lalu mereset flag ke belum ada (precondition "flag seen belum ada" TC-GS-POS-16, 18, 19, dan 20). Flag di-reset ulang sebagai langkah penghubung sebelum TC-GS-POS-18, 19, dan 20 karena TC sebelumnya menutup walkthrough dan menandai seen, dan disetel ke true sebagai langkah penghubung sebelum TC-GS-POS-21 (precondition "flag sudah true"). Hook `after` memulihkan nilai awal flag. Mekanisme baca, reset, penyetelan, dan pemulihan flag lewat API disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan nilai awal flag akun Total Control.
- Kemampuan teknis: klik pada area overlay gelap di luar tooltip box (koordinat di luar spotlight dan tooltip); pembacaan state flag lewat perilaku kunjungan ulang tab Position.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-16: Guided Tooltip muncul otomatis pada kunjungan pertama

1. Buka Global Settings > User dari sidebar Global Settings
2. Klik sub-tab Position
3. Verifikasi walkthrough otomatis mulai di Step 1
4. Verifikasi spotlight pada Table Tools
5. Verifikasi Step 1 Title "Table Tools"
6. Verifikasi Step 1 Description "Search, filter, and download the positions in this list."
7. Verifikasi indikator "Step 1 of 3" tampil
8. Verifikasi indikator "Step 1 of 3" berada di atas title
9. Verifikasi tombol `[Skip]` tampil
10. Verifikasi tombol `[Next]` tampil
11. Verifikasi tombol `[Back]` Hidden di Step 1
12. Verifikasi area selain spotlight tertutup overlay gelap
13. Klik `[Skip]` untuk menutup walkthrough
14. Reset flag `guided_tooltip_seen_gs-position` akun Total Control ke belum ada

### TC-GS-POS-18: Guided Tooltip, Done menutup dan tidak muncul otomatis lagi

15. Klik sub-tab User List
16. Klik sub-tab Position
17. Klik `[Next]`
18. Klik `[Next]`
19. Klik `[Done]`
20. Verifikasi walkthrough tertutup setelah `[Done]`
21. Klik sub-tab User List
22. Klik sub-tab Position
23. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya
24. Reset flag `guided_tooltip_seen_gs-position` akun Total Control ke belum ada

### TC-GS-POS-19: Guided Tooltip, Skip via tombol menutup dan menandai seen

25. Klik sub-tab User List
26. Klik sub-tab Position
27. Klik `[Skip]` di Step 1
28. Verifikasi walkthrough tertutup
29. Klik sub-tab User List
30. Klik sub-tab Position
31. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya
32. Reset flag `guided_tooltip_seen_gs-position` akun Total Control ke belum ada

### TC-GS-POS-20: Guided Tooltip, klik overlay gelap setara Skip

33. Klik sub-tab User List
34. Klik sub-tab Position
35. Klik area overlay gelap di luar tooltip box
36. Verifikasi walkthrough tertutup
37. Klik sub-tab User List
38. Klik sub-tab Position
39. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya
40. Setel flag `guided_tooltip_seen_gs-position` akun Total Control ke true

### TC-GS-POS-21: Guided Tooltip, replay via tombol [?]

41. Klik tombol `[?]` di samping breadcrumb
42. Verifikasi walkthrough mulai dari Step 1 dengan spotlight pada Table Tools
43. Klik `[Skip]`
44. Klik sub-tab User List
45. Klik sub-tab Position
46. Verifikasi walkthrough tidak muncul otomatis (flag seen tidak di-reset oleh replay)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti TC sumber (16, 18, 19, 20, 21). TC-GS-POS-21 ditaruh terakhir karena precondition-nya flag sudah true. Konten step, navigasi Next/Back, resize viewport, keyboard, dan aktor Read Only diuji di spec 005 (TC-GS-POS-17, 22, 23, 24).
- TC-GS-POS-16 memakai flag belum ada dari hook `before`; TC-GS-POS-18, 19, dan 20 masing-masing butuh flag belum ada sehingga di-reset di akhir TC sebelumnya.
- "Kunjungan berikutnya" dan "buka ulang tab Position" dilakukan dengan klik sub-tab User List lalu Position; "keluar ke menu lain" pada TC-GS-POS-18 dilakukan dengan klik sub-tab User List.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik sub-tab User List lalu Position untuk memicu kunjungan, klik `[Skip]` penutup pada langkah 13, reset flag pada langkah 14, 24, dan 32, serta penyetelan flag ke true pada langkah 40.
- Spec 006 dipisah dari spec 005 (Guided Tooltip tab Position yang sama): gabungannya 113 langkah (67 dan 46), jauh di atas sekitar 35 langkah, dan tiap blok mereset atau menyetel flag seen sendiri sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Spec melewati sekitar 35 langkah (46 langkah). Seluruhnya satu kelas (Guided Tooltip tab Position: flag seen dan dismiss), tiap blok TC berdiri sendiri karena flag di-reset atau disetel sebelum tiap blok, dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-POS-16, 18, 19, 20, dan 21 mensyaratkan flag seen belum ada atau sudah true tanpa menyebut cara menyetelnya; mekanismenya disediakan tim FE/BE.
  - TC-GS-POS-18 menyebut "keluar ke menu lain" tanpa menyebut menu yang dipakai; spec memakai sub-tab User List.
  - TC-GS-POS-20 tidak menyebut titik klik pada overlay gelap; spec mengklik area overlay di luar spotlight dan tooltip box.
  - TC-GS-POS-16 butir b mencantumkan Title dan Description Step 1, sedangkan Expected TC-GS-POS-21 hanya menyebut "Step 1 (Table Tools)"; spec TC-GS-POS-21 mengasersi Step 1 dan spotlight Table Tools tanpa Description.
