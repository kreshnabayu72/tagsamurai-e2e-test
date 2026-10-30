---
id: TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save
title: "Edit Position: Duplikat saat Mengetik dan Save, Nama Sendiri Bukan Duplikat, Saving State, dan Klik Ganda Save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-85
  - TC-GS-POS-86
  - TC-GS-POS-87
  - TC-GS-POS-104
  - TC-GS-POS-105
coverage:
  web: automated
---

# Edit Position: Duplikat saat Mengetik dan Save, Nama Sendiri Bukan Duplikat, Saving State, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE (backend nyata). Kasus saving state (TC-GS-POS-104) memakai intercept parsial di atas backend nyata.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`.
- Data Pre-setup (tidak diubah spec ini, tanpa suffix): Position 11 `Finance Analyst` sebagai nama pembanding duplikat.
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.editSeed017`; nama bersuffix):
  - `Legal Counsel {runId}-017` untuk TC-GS-POS-85, 86, 87 (nama tidak berubah).
  - `Marketing Executive {runId}-017` untuk TC-GS-POS-104; diubah menjadi `Marketing Lead {runId}-017`, lalu menjadi `Marketing Manager {runId}-017` pada TC-GS-POS-105.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-017` yang masih ada (`Legal Counsel`, `Marketing Executive`, `Marketing Lead`, `Marketing Manager`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Edit Position 3 detik dan melepasnya sesudahnya (TC-GS-POS-104; TC menyebut "diperlambat via DevTools"); jeda debounce ±500 ms untuk pengecekan duplikat (jeda pendek, ditunggu nyata); klik ganda cepat pada `[Save]` (TC-GS-POS-105); membaca status disabled dan spinner tombol serta input.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite). Intercept dilepas pada langkah 27 dan di hook `after`.

## Test Steps

### TC-GS-POS-85: Nama duplikat case-insensitive terdeteksi saat mengetik

1. Ketik Search `{runId}-017`, tekan Enter
2. Klik `⋯` pada baris `Legal Counsel {runId}-017`, pilih `Edit`
3. Verifikasi Popup Edit Position terbuka
4. Ganti nilai Position Name dengan `finance analyst`, tunggu ±500 ms tanpa blur
5. Verifikasi error inline "Position Name already exists" muncul ±500 ms setelah berhenti mengetik

### TC-GS-POS-86: Nama duplikat dengan spasi depan dan belakang ditolak saat Save

6. Ketik ulang `Legal Counsel {runId}-017` pada input Position Name (agar error dari langkah 4 hilang)
7. Ganti nilai dengan `  Finance Analyst  `
8. Klik `[Save]`
9. Verifikasi error inline "Position Name already exists"
10. Verifikasi Save ditolak
11. Verifikasi Popup Edit tetap terbuka

### TC-GS-POS-87: Nama sendiri tidak dianggap duplikat

12. Hapus seluruh teks Position Name, lalu ketik ulang `Legal Counsel {runId}-017`, tunggu ±500 ms
13. Verifikasi tidak ada error "Position Name already exists"
14. Klik `✕` pada Popup Edit (nilai sama dengan nilai tersimpan, tanpa dialog)

### TC-GS-POS-104: Saving state saat Save diproses

15. Pasang intercept yang menahan respons Edit Position selama 3 detik
16. Klik `⋯` pada baris `Marketing Executive {runId}-017`, pilih `Edit`
17. Verifikasi Popup Edit Position terbuka
18. Ganti nilai menjadi `Marketing Lead {runId}-017`
19. Klik `[Save]`
20. Verifikasi `[Save]` menampilkan spinner
21. Verifikasi `[Save]` disabled
22. Verifikasi input Position Name disabled
23. Verifikasi `[Clear Field]` disabled
24. Verifikasi `[✕]` disabled
25. Verifikasi setelah respons kembali, toast sukses "Success, position has been updated."
26. Verifikasi Popup Edit tertutup
27. Lepas intercept penahan respons

### TC-GS-POS-105: Klik ganda Save hanya diproses sekali

28. Tunggu toast dari langkah 25 hilang otomatis
29. Klik `⋯` pada baris `Marketing Lead {runId}-017`, pilih `Edit`
30. Verifikasi Popup Edit Position terbuka
31. Ganti nilai menjadi `Marketing Manager {runId}-017`
32. Klik `[Save]` dua kali cepat
33. Verifikasi hanya satu toast sukses yang tampil: "Success, position has been updated."
34. Verifikasi tidak ada error "Position Name already exists"
35. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 85, 86, 87, 104, 105 (sama dengan TC sumber). Validasi yang diblokir (TC-GS-POS-85, 86, 87) memakai satu pembukaan popup; TC-GS-POS-104 dan 105 mengubah data sehingga ditaruh sesudahnya. Jumlah pembukaan popup: 3 (langkah 2, 16, 29); jumlah penutupan: 3 (langkah 14, 26, dan penutupan otomatis setelah Save sukses pada langkah 32).
- TC-GS-POS-105 mensyaratkan record `Marketing Lead` yang dihasilkan TC-GS-POS-104; langkah 15 sampai 27 (rename dari `Marketing Executive`) disalin ke spec ini sehingga record tersebut dibuat oleh spec sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search agar baris target tampil pada halaman aktif), langkah 6 (mengembalikan nilai tersimpan agar error dari langkah 4 tidak mengaburkan asersi berikutnya), langkah 14 (menutup form bersih), langkah 15 dan 27 (memasang dan melepas intercept), langkah 28 (menunggu toast sukses TC-GS-POS-104 hilang otomatis supaya hitungan toast TC-GS-POS-105 pada langkah 33 tidak terpengaruh), dan langkah 35 (menutup input Search dan mereset tabel).
- Langkah 14 menutup popup lewat `✕` tanpa `Verifikasi` dialog karena nilai sudah kembali identik dengan nilai tersimpan (perilaku tidak dirty diuji TC-GS-POS-99, bukan di spec ini).
- Langkah 3, 17, dan 30 adalah `Verifikasi` dari anotasi "→ Popup Edit Position terbuka" pada Langkah 1 TC.
- Asersi state sementara (spinner dan disabled) pada langkah 20 sampai 24 dibuat selama respons ditahan, sebelum langkah 25.
- Spec berisi 35 langkah dan tidak melewati batas smell sekitar 35 langkah.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-86 ("Nama record tetap `Legal Counsel`"), TC-GS-POS-104 ("Record bernama `Marketing Lead`"), dan TC-GS-POS-105 ("Changelog: Position mencatat tepat 1 entri Edit") tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-85 Expected menyebut ±500 ms tanpa batas toleransi; spec menunggu ±500 ms nyata pada langkah 4 dan 12 lalu mengasersi.
  - TC-GS-POS-105 Expected "Tidak ada error duplikat" tidak menyebut permukaannya (inline atau toast); spec mengasersi tidak ada error "Position Name already exists" pada layar setelah toast.
  - TC-GS-POS-104 menyebut "Respons edit diperlambat via DevTools"; spec memakai intercept untuk menahan respons 3 detik.
