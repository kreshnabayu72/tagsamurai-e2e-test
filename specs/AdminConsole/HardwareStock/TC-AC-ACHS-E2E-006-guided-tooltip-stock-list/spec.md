---
id: TC-AC-ACHS-E2E-006-guided-tooltip-stock-list
title: "Guided Tooltip Stock List: Isi Step, Replay, Skip, Resize, dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-25
  - TC-AC-ACHS-26
  - TC-AC-ACHS-27
  - TC-AC-ACHS-28
  - TC-AC-ACHS-29
coverage:
  web: automated
---

# Guided Tooltip Stock List: Isi Step, Replay, Skip, Resize, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris Stock List (No 16). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Guided Tooltip (spec yang menguji flag itu sendiri): spec ini mengatur flag `seen` halaman Stock List (flag `guided_tooltip_seen` untuk `ac-hardware-stock` pada TC; nama dan `page_key` dikonfirmasi tim FE/BE) untuk akun aktor sesudah hook suite `before` menyetelnya true. Kemampuan menyetel flag menjadi false dan true lewat sesi API aktor disediakan tim FE/BE; hook suite `after` memulihkan nilai awal flag.
- Kemampuan teknis (disediakan tim FE): memuat ulang halaman (F5), mengubah dan memulihkan ukuran viewport browser, input keyboard (Enter, panah kiri, panah kanan, Esc).
- State global yang diubah: flag `seen` Guided Tooltip halaman Stock List akun aktor (dipulihkan oleh hook suite `after`).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-25: Empat step tampil verbatim saat kunjungan pertama

1. Setel flag `seen` halaman Stock List akun aktor menjadi false
2. Klik menu Hardware > Stock di sidebar
3. Verifikasi walkthrough Step 1 menargetkan Table (Stock List)
4. Verifikasi Step 1 Title "Hardware Stock Overview"
5. Verifikasi Step 1 Description "This page tracks all physical hardware inventory owned by your organization, grouped by SKU — from initial receipt through deployment to clients."
6. Verifikasi `[Back]` tersembunyi di Step 1
7. Klik `[Next]`
8. Verifikasi Step 2 menargetkan Table — Kolom Total Registered, Available & In Use
9. Verifikasi Step 2 Title "Stock Quantities"
10. Verifikasi Step 2 Description "Monitor registered stock balances, units ready to deploy, and active deployments. Available indicates units not yet activated; In Use indicates units activated by clients."
11. Klik `[Next]`
12. Verifikasi Step 3 menargetkan Toolbar TableTools — Search & Filter
13. Verifikasi Step 3 Title "Search & Filters"
14. Verifikasi Step 3 Description "Quickly locate hardware SKUs by searching or narrowing down the list with filters."
15. Klik `[Next]`
16. Verifikasi Step 4 menargetkan Table — Kolom Actions
17. Verifikasi Step 4 Title "Stock Management Actions"
18. Verifikasi Step 4 Description "Use row actions to work with each SKU's stock."
19. Verifikasi `[Next]` berubah menjadi `[Done]` di Step 4
20. Klik `[Done]`
21. Verifikasi walkthrough tertutup

### TC-AC-ACHS-26: Kunjungan berikutnya tidak otomatis, tombol `[?]` memutar ulang tanpa mereset flag

22. Tekan F5
23. Verifikasi Breadcrumb `Hardware > Stock` tampil
24. Verifikasi walkthrough tidak muncul otomatis
25. Klik tombol `[?]` di sebelah kanan breadcrumb
26. Verifikasi walkthrough mulai dari Step 1
27. Klik `[Skip]`
28. Tekan F5
29. Verifikasi Breadcrumb `Hardware > Stock` tampil
30. Verifikasi walkthrough tetap tidak muncul otomatis

### TC-AC-ACHS-27: Skip lewat tombol dan lewat klik overlay menutup dan menyimpan flag seen

31. Setel flag `seen` halaman Stock List akun aktor menjadi false
32. Klik menu Hardware > Stock di sidebar
33. Klik `[Skip]` pada Step 1
34. Verifikasi walkthrough tertutup
35. Setel flag `seen` halaman Stock List akun aktor menjadi false
36. Klik menu Hardware > Stock di sidebar
37. Klik area overlay gelap di luar tooltip
38. Verifikasi walkthrough tertutup
39. Tekan F5
40. Verifikasi Breadcrumb `Hardware > Stock` tampil
41. Verifikasi walkthrough tidak muncul otomatis (flag seen ter-set)

### TC-AC-ACHS-28: Resize atau navigasi keluar di tengah walkthrough tidak menyimpan flag seen

42. Setel flag `seen` halaman Stock List akun aktor menjadi false
43. Klik menu Hardware > Stock di sidebar
44. Klik `[Next]` ke Step 2
45. Ubah ukuran viewport browser
46. Verifikasi walkthrough tertutup
47. Kembalikan ukuran viewport browser ke ukuran semula
48. Tekan F5
49. Verifikasi walkthrough muncul lagi dari Step 1 (flag seen tidak ter-set oleh resize)
50. Klik `[Next]` ke Step 2
51. Klik `[Next]` ke Step 3
52. Klik menu Approvals > Hardware Stock di sidebar
53. Klik menu Hardware > Stock di sidebar
54. Verifikasi walkthrough muncul lagi dari Step 1 (flag seen tidak ter-set oleh navigasi keluar)

### TC-AC-ACHS-29: Aksesibilitas keyboard

55. Klik `[Skip]` pada Step 1
56. Klik tombol `[?]` di sebelah kanan breadcrumb
57. Verifikasi kotak tooltip menerima fokus keyboard
58. Tekan Enter
59. Verifikasi walkthrough pindah ke Step 2 (Enter = Next)
60. Tekan panah kiri
61. Verifikasi walkthrough kembali ke Step 1 (panah kiri = Back)
62. Tekan panah kanan
63. Verifikasi walkthrough pindah ke Step 2 (panah kanan = Next)
64. Tekan Esc
65. Verifikasi walkthrough tertutup (Esc = Skip)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-25, 26, 27, 28, 29). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 31, 35, dan 42 (menyetel flag `seen` ke false, pengganti "Reset flag" dan precondition kunjungan pertama), langkah 2, 32, 36, dan 43 (membuka halaman lewat sidebar), langkah 47 (memulihkan viewport, S-09), langkah 55 (menutup walkthrough yang tersisa dari TC-28 sebelum TC-29).
- Langkah 23 dan 29 dan 40 adalah anchor positif (halaman Stock List termuat) untuk asersi absence walkthrough (bagian 8b butir 2); Expected TC tidak memuatnya.
- Spec di atas smell 35 langkah (65 langkah). Alasan: seluruh blok adalah satu topik Guided Tooltip halaman Stock List dengan flag yang sama, kelima TC berdiri sendiri, dan empat step verbatim pada TC-25 saja menghabiskan 19 langkah karena satu `Verifikasi` per klausa (target, Title, Description).
- Temuan untuk QA:
  - Nama dan `page_key` flag `guided_tooltip_seen` untuk `ac-hardware-stock` tidak didefinisikan di TC, PRD, atau LLD yang dibaca; mekanisme menyetel flag diminta dari tim FE/BE.
  - TC-27 langkah 3 ("Reset flag lalu buka halaman lagi") tidak menyebut cara reset; spec memakai kemampuan menyetel flag. Expected b ("setelah muat ulang walkthrough tidak muncul otomatis") hanya diamati sesudah Skip lewat overlay (langkah 39 sampai 41); flag seen sesudah Skip lewat tombol tidak diamati terpisah oleh TC.
  - TC-28 langkah 3 ("Ubah ukuran viewport") tidak menyebut ukuran; spec memakai ukuran yang disediakan tim FE. TC-28 langkah 5 ("menu sidebar lain") tidak menyebut menu; spec memakai Approvals > Hardware Stock.
  - TC-29 Expected a ("kotak tooltip menerima fokus keyboard") tidak menyebut elemen yang diperiksa; spec mengasersi fokus pada kotak tooltip.
