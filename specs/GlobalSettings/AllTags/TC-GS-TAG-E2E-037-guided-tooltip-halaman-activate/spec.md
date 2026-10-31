---
id: TC-GS-TAG-E2E-037-guided-tooltip-halaman-activate
title: "Guided Tooltip Halaman Activate TAG: Empat Step per Tipe Sesi dan Replay [?]"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-114
coverage:
  web: automated
---

# Guided Tooltip Halaman Activate TAG: Empat Step per Tipe Sesi dan Replay [?]

## Prerequisites

- Mode: FE+BE (backend nyata; flag Guided Tooltip disimpan di backend).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada ganti akun.
- Guided Tooltip (page_key `gs-tag-activate`): spec ini menguji flag `guided_tooltip_seen_gs-tag-activate` sendiri sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`). Hook `before` mencatat nilai awal flag akun Total Control Client A lalu menyetelnya menjadi belum true (precondition TC-GS-TAG-114); hook `after` memulihkan nilai awal. Mekanisme membaca dan menyetel flag disediakan tim FE/BE (S-13).
- Data: tidak ada Data Pre-setup maupun Dinamis yang diasersi; sesi Activate GPS dibuka tanpa menambah baris. Opsi mandiri (BYO) Client A aktif (section `Self-Purchased Template` tidak terkunci dan disorot pada Step 1).
- Kemampuan teknis (disediakan tim FE/BE): baca dan setel flag Guided Tooltip per akun; sorotan (spotlight) elemen diamati lewat selektor yang disediakan tim FE. PRD menetapkan target tur Activate `#activate-template`, `#activate-staging-table`, `#btn-submit-activation`, dan `#btn-scan-tag`; kontrol masuk data GPS (input entri manual dan unggah) tidak punya ID di sumber.
- Pemulihan di hook `after` (tidak berasumsi setup berhasil penuh): pulihkan nilai awal flag `guided_tooltip_seen_gs-tag-activate`, buang staging bila ada.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Spec hanya mengubah flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-TAG-114: Guided tooltip halaman Activate TAG, empat step dan replay

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Verifikasi tur otomatis tampil pada Step 1 `Self-Purchased Template` dengan teks "Fill this in once at the start for TAGs that are not in your official stock."
3. Verifikasi Step 1 menyorot elemen yang tampil pada sesi GPS (Template Self-Purchased)
4. Klik [Next]
5. Verifikasi Step 2 `Scan TAG` dengan teks "Scan TAGs one by one or in bulk. For GPS, upload a file or enter IMEIs manually."
6. Verifikasi Step 2 menyorot kontrol masuk data GPS (input entri manual dan unggah)
7. Klik [Next]
8. Verifikasi Step 3 `Staging Table` dengan teks "Review each row and its status before submitting."
9. Verifikasi Step 3 menyorot elemen yang tampil pada sesi GPS (tabel staging)
10. Klik [Next]
11. Verifikasi Step 4 `Submit` dengan teks "Activate all valid TAGs in the table."
12. Verifikasi Step 4 menyorot elemen yang tampil pada sesi GPS (tombol Submit)
13. Klik [Done]
14. Klik ikon `[?]`
15. Verifikasi tur dimulai ulang dari Step 1 `Self-Purchased Template`
16. Verifikasi flag `guided_tooltip_seen_gs-tag-activate` tetap true (tidak direset oleh `[?]`)
17. Tutup tur dengan klik `Skip`

## Notes

- Mode: FE+BE. Spec berisi satu TC, 17 langkah (di bawah batas 35).
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1 (membuka sesi yang memicu tur), 4, 7, 10, 13, 14 (navigasi tur dan replay sesuai Langkah Uji TC), 17 (menutup tur yang terbuka akibat replay sebelum spec berakhir).
- Pembagian TC lintas spec: Guided Tooltip registri (`gs-tag-registry`) berada di spec 005.
- Temuan untuk QA:
  - Judul spec "per Tipe Sesi" mengikuti pengelompokan topik; TC-GS-TAG-114 hanya menjalankan sesi GPS. Expected e menyebut elemen yang disorot "pada tipe sesi aktif" tanpa menetapkan elemen per tipe selain GPS step 2; sesi RFID, NFC, dan BLE tidak diuji.
  - Expected e tidak menyebut selektor atau ID sorotan per step; asersi sorotan memakai selektor yang disediakan tim FE.
  - Expected f ("tanpa mereset flag seen") tidak punya cara observasi di TC; spec membaca flag lewat kemampuan yang disediakan tim FE/BE (langkah 16), tanpa endpoint karangan.
