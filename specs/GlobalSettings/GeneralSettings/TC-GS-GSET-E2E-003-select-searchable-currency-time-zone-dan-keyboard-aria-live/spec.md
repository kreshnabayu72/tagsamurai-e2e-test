---
id: TC-GS-GSET-E2E-003-select-searchable-currency-time-zone-dan-keyboard-aria-live
title: "Select Searchable + keyboard + aria-live"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-09
  - TC-GS-GSET-10
  - TC-GS-GSET-13
coverage:
  web: automated
---

# Select Searchable + keyboard + aria-live

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`.
- Data Pre-setup No 10 (record Client A) dan No 12 sampai 13: Currency Code `IDR` (label `Rp - Indonesian Rupiah`), `EUR` (label, nama, dan simbol ditentukan programmer, NC-10); Time Zone `Asia/Jakarta` (label `(UTC+07:00) Bangkok, Hanoi, Jakarta`, PRD §4.3a). `[simbol opsi EUR]` adalah simbol yang tampil pada label opsi `EUR`, dibaca dari dropdown saat memilih (langkah 8), bukan literal. Kata kunci pencarian: `Dollar`, `Euro`, `Bangkok`, `Hanoi`, `zzzz`.
- Kemampuan teknis: operasi keyboard (`Tab`, `Enter`, ketik) pada Select dan pembacaan atribut `aria-live` pada elemen DOM Preview.
- Spec tidak menekan `[Save]`; pilihan `EUR` hanya ada di form dan dikembalikan ke `IDR` di langkah 21 (lalu dipilih ulang `EUR` di langkah 26 sampai 27) dan dikembalikan lagi ke `IDR` di langkah 29, sehingga form identik dengan nilai tersimpan dan tidak ada perubahan belum disimpan saat spec berikutnya membuka halaman. Tidak ada state global yang diubah.

## Test Steps

### TC-GS-GSET-09: Select Currency Code Searchable

1. Klik Select "Currency Code"
2. Verifikasi label tiap opsi berformat "[Symbol] - [Currency Name]" (simbol tampil di label opsi sendiri)
3. Verifikasi tidak ada opsi "Other"
4. Ketik "Dollar" di kotak pencarian Select
5. Verifikasi sedikitnya satu opsi tampil dan label setiap opsi yang tampil memuat "Dollar"
6. Hapus kata kunci lalu ketik "Euro"
7. Verifikasi opsi untuk kode `EUR` tampil
8. Pilih opsi untuk kode `EUR` dan catat label opsinya sebagai `label opsi EUR` serta simbolnya sebagai `[simbol opsi EUR]`
9. Verifikasi field "Currency Code" menampilkan `label opsi EUR`
10. Verifikasi tidak ada field "Currency Symbol" terpisah

### TC-GS-GSET-10: Select Time Zone Searchable

11. Klik Select "Time Zone"
12. Catat label opsi Time Zone yang terpilih (default `Asia/Jakarta`: `(UTC+07:00) Bangkok, Hanoi, Jakarta`)
13. Verifikasi label tiap opsi berformat "(UTC±HH:MM) City1, City2, City3"
14. Ketik "Bangkok" di kotak pencarian Select
15. Verifikasi opsi `Asia/Jakarta` (`(UTC+07:00) Bangkok, Hanoi, Jakarta`) tampil
16. Hapus kata kunci lalu ketik "Hanoi"
17. Verifikasi opsi `Asia/Jakarta` (`(UTC+07:00) Bangkok, Hanoi, Jakarta`) tampil
18. Hapus kata kunci lalu ketik "zzzz"
19. Verifikasi tidak ada opsi yang cocok
20. Tutup dropdown dengan `Esc`

### TC-GS-GSET-13: Accessibility Preview dan keyboard Select

21. Pilih Currency Code `IDR` lewat dropdown agar Preview Currency kembali ke "Rp 5.000,00"
22. Verifikasi elemen Preview Currency memiliki atribut `aria-live` (live region)
23. Verifikasi elemen Preview Date & Time memiliki atribut `aria-live` (live region)
24. Tekan `Tab` hingga fokus pada Select "Currency Code", tekan `Enter`
25. Verifikasi Select "Currency Code" dapat difokus dan dibuka via keyboard
26. Ketik "Euro", tekan `Enter`
27. Verifikasi Select "Currency Code" dapat dicari dan dipilih via keyboard (field menampilkan `label opsi EUR`)
28. Verifikasi Preview Currency "[simbol opsi EUR] 5.000,00"
29. Pilih kembali Currency Code `IDR` lewat dropdown

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 29 langkah.
- Langkah penghubung (tanpa `Verifikasi`): langkah 12 (mencatat label opsi Time Zone terpilih), langkah 20 (menutup dropdown Time Zone), langkah 21 (mengembalikan Currency Code ke `IDR` supaya perubahan Preview Currency pada langkah 28 teramati dan tidak terbawa dari TC-GS-GSET-09, S-09), dan langkah 29 (mengembalikan Currency Code ke `IDR` sehingga form tidak dirty di akhir spec, S-09).
- TC-GS-GSET-10 langkah 1 hanya meminta mencatat label opsi yang terpilih; label itu dicatat di langkah 12 tanpa `Verifikasi` (label dikunci PRD §4.3a, S-03) dan Expected a (format label tiap opsi) diasersi sendiri di langkah 13.
- TC-GS-GSET-09 langkah 4 ("Hapus kata kunci lalu ketik Euro") dan TC-GS-GSET-10 langkah 3 dan 4 dipecah per aksi; asersi absence (langkah 3, 19) didahului asersi atas daftar opsi pada dropdown yang sama (langkah 2, 5, 15, 17).
- Asersi universal langkah 5 (setiap opsi memuat "Dollar") didahului pembanding "sedikitnya satu opsi tampil" pada kalimat yang sama.
- Temuan untuk QA:
  - TC-GS-GSET-10 meminta mengetik "salah satu nama kota yang ada di label opsi terpilih" tanpa menyebut nama. Spec memakai `Bangkok` dan `Hanoi` dari label opsi `Asia/Jakarta` yang dikunci PRD §4.3a (daftar opsi Time Zone lain ditentukan programmer, NC-09).
  - Label opsi `EUR` tidak dikunci di PRD (NC-10); spec membaca label dari dropdown saat memilih (langkah 8) dan memakainya pada langkah 9, 27, dan 28.
  - TC-GS-GSET-13 Expected a meminta atribut `aria-live` tanpa menyebut nilainya (`polite` atau `assertive`); spec hanya mengasersi atribut ada.
