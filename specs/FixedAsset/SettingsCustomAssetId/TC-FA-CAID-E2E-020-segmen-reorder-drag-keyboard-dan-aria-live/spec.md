---
id: TC-FA-CAID-E2E-020-segmen-reorder-drag-keyboard-dan-aria-live
title: "Daftar Segmen: Reorder Drag, Keyboard, dan Aria-Live Live Preview"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-65
  - TC-FA-CAID-66
  - TC-FA-CAID-67
coverage:
  web: automated
---

# Daftar Segmen: Reorder Drag, Keyboard, dan Aria-Live Live Preview

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): drag-and-drop pada drag handle baris segmen; keyboard reorder (Tab, `Spacebar`, panah `Up` dan `Down`); inspeksi atribut DOM elemen Live Preview dan pengamatan pembaruan live region pada elemen itu (langkah 15 sampai 18). Pengamatan dilakukan lewat DOM, tanpa pembaca layar.
- Spec hanya mengamati: tidak menekan `[Save]`, tidak membuat data, tidak mengubah state global. Satu pembukaan form dipakai untuk seluruh TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-65: Drag baris segmen memperbarui Live Preview tanpa jeda dan mengaktifkan Save

1. Seret drag handle baris `Purchase Date (MMYY)` ke atas baris `Group Code`
2. Verifikasi baris `Purchase Date (MMYY)` berpindah ke posisi di atas `Group Code`
3. Verifikasi Live Preview langsung menampilkan `0926/JKT/LAP/T490/1`
4. Verifikasi tombol `[Save]` aktif
5. Seret drag handle baris `Purchase Date (MMYY)` kembali ke posisi di bawah `Asset Name Code` dan di atas `Asset Increment`

### TC-FA-CAID-66: Reorder segmen dengan keyboard

6. Fokuskan drag handle baris `Group Code` dengan Tab
7. Tekan `Spacebar`
8. Tekan panah `Down` satu kali
9. Verifikasi baris `Group Code` bertukar posisi dengan baris `Category Code` sehingga urutan menjadi `Category Code`, `Group Code`, `Asset Name Code`
10. Verifikasi Live Preview menampilkan `LAP/JKT/T490/0926/1`
11. Tekan panah `Up` satu kali
12. Verifikasi baris `Group Code` kembali di atas `Category Code`
13. Verifikasi Live Preview kembali menampilkan `JKT/LAP/T490/0926/1`
14. Lepaskan fokus dari daftar segmen dengan mengklik area kosong halaman

### TC-FA-CAID-67: Kotak Live Preview memiliki aria-live polite

15. Inspeksi atribut elemen kotak Live Preview
16. Verifikasi elemen Live Preview memiliki atribut `aria-live="polite"`
17. Hilangkan centang `Purchase Date (MMYY)`
18. Verifikasi perubahan teks Live Preview menjadi `JKT/LAP/T490/1` terkirim sebagai pembaruan live region
19. Centang kembali `Purchase Date (MMYY)`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5 (mengembalikan urutan segmen ke baseline), langkah 14 (melepaskan fokus daftar segmen), dan langkah 19 (memulihkan segmen Purchase Date). Form tidak pernah disimpan; di akhir spec urutan dan centang segmen sama dengan nilai tersimpan.
- Temuan untuk QA:
  - G-3 di catatan TC: tepi keyboard reorder (`Spacebar` kedua, `Esc`, ujung daftar, aturan jatuh) tidak dinyatakan PRD. Cara menjatuhkan item sesudah langkah 11 tidak diberikan TC, sehingga langkah 14 (klik area kosong) adalah langkah penghubung yang dipilih spec, bukan perilaku yang diasersi.
  - TC-FA-CAID-67 b ("terkirim sebagai pembaruan live region") tidak menyebut cara pengamatannya; spec mengamati lewat DOM sebagai kemampuan yang disediakan tim FE.
