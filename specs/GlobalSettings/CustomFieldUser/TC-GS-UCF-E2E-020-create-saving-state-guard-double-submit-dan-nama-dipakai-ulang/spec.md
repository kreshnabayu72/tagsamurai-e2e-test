---
id: TC-GS-UCF-E2E-020-create-saving-state-guard-double-submit-dan-nama-dipakai-ulang
title: "Create Custom Field: Saving State, Guard Klik Ganda Submit, dan Field Name Dipakai Ulang Setelah Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-83
  - TC-GS-UCF-84
  - TC-GS-UCF-455
coverage:
  web: automated
---

# Create Custom Field: Saving State, Guard Klik Ganda Submit, dan Field Name Dipakai Ulang Setelah Dihapus

## Prerequisites

- Mode: FE+BE (backend nyata). TC-GS-UCF-83 memakai intercept parsial di atas backend nyata (menahan respons Create); bukan `Mode: mock`.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup: tidak ada yang dibaca atau diubah.
- Data dinamis (`{runId}` terdiri atas digit):
  - D-20: `Slow One {runId}-020` (Text), dibuat lewat UI oleh TC-GS-UCF-83.
  - D-21: `Twice {runId}-020` (Text), dibuat lewat UI oleh TC-GS-UCF-84.
  - D-189: `Reuse Name Probe {runId}-020` (Text, Active), di-seed lewat API di hook `before` (precondition TC-GS-UCF-455), dihapus lewat UI oleh spec, lalu dibuat ulang lewat UI dengan nama yang sama.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Client A yang namanya memuat `{runId}-020`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Create Custom Field 3 detik dan melepas intercept sesudahnya (TC-GS-UCF-83); klik ganda cepat pada [Submit] (TC-GS-UCF-84); hover tombol; jeda ±500 ms untuk debounce keunikan; Search pada tabel dan Changelog.
- State global: tidak ada yang diubah (intercept dilepas di langkah 14 dan di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-83: Tombol Submit menampilkan hover dan Saving state selama request berlangsung

1. Klik [+ Custom Field]
2. Isi Field Name `Slow One {runId}-020`, Data Type `Text`
3. Hover [Submit]
4. Verifikasi hover menampilkan state hover tombol [Submit]
5. Pasang intercept yang menahan respons Create Custom Field selama 3 detik
6. Klik [Submit]
7. Verifikasi [Submit] menampilkan loading
8. Verifikasi [Submit] disabled
9. Verifikasi `[Clear Field]` disabled
10. Verifikasi icon `[✕]` disabled
11. Verifikasi input Field Name disabled
12. Verifikasi setelah respons kembali, popup tertutup
13. Verifikasi toast sukses: "Success, custom field has been created."
14. Lepas intercept penahan respons

### TC-GS-UCF-84: Klik ganda [Submit] hanya membuat satu Custom Field

15. Klik [+ Custom Field]
16. Isi Field Name `Twice {runId}-020`, Data Type `Text`
17. Klik [Submit] dua kali cepat
18. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been created."
19. Ketik Search `Twice {runId}-020`, tekan Enter
20. Verifikasi hanya 1 baris `Twice {runId}-020` di tabel
21. Klik icon Changelog
22. Ketik Search `Twice {runId}-020` di Changelog, tekan Enter
23. Verifikasi Changelog memuat 1 entri Create untuk `Twice {runId}-020`
24. Tutup modal Changelog

### TC-GS-UCF-455: Field Name dapat dipakai ulang setelah field dengan nama itu dihapus

25. Ganti isi kotak search dengan `Reuse Name Probe {runId}-020`, tekan Enter
26. Klik `⋯` pada baris `Reuse Name Probe {runId}-020` > Delete
27. Klik [Delete]
28. Verifikasi toast sukses: "Success, custom field has been deleted."
29. Klik [+ Custom Field]
30. Ketik `Reuse Name Probe {runId}-020` di Field Name, tunggu ±500 ms
31. Verifikasi tidak ada error `Field name already exists`
32. Pilih Data Type `Text`
33. Klik [Submit]
34. Verifikasi toast sukses: "Success, custom field has been created."
35. Verifikasi baris `Reuse Name Probe {runId}-020` tampil dengan switch Active On

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 83, 84, 455 (sama dengan sumber). TC-GS-UCF-455 menghapus data (Delete) dan ditaruh paling akhir (bagian 3 prinsip 5); data yang dihapus milik spec (D-189), bukan data Pre-setup.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 14 (memasang dan melepas intercept), langkah 19, 22, 25 (Search), langkah 21 dan 24 (membuka dan menutup Changelog), serta pengisian form dan klik tombol sebagai bagian langkah TC. Asersi saving state diletakkan sebelum popup tertutup (langkah 7 sampai 11) sesuai bagian 8b butir 5.
- TC-GS-UCF-83 dan 84 membagi pembukaan popup sendiri-sendiri karena Submit tanpa Stay menutup popup; TC-GS-UCF-455 membuka popup ketiga. Tidak ada kejadian menutup form lain yang diuji di spec ini.
- Changelog `Twice {runId}-020` memakai nama unik sehingga jumlah entri dihitung dengan baseline nol (S-12).
- Temuan untuk QA:
  - TC-GS-UCF-83 menyebut "Tunda respons POST 3 detik" tanpa endpoint; intercept ditulis tanpa mengarang endpoint (mekanisme mengikuti kemampuan `Spectra.intercept()` tim FE).
  - TC-GS-UCF-83 Expected "input disabled" tidak merinci input mana; spec mengasersi input Field Name.
  - TC-GS-UCF-455 tidak menyebut teks konfirmasi dialog Delete; langkah mengikuti TC ("Klik [Delete]").
