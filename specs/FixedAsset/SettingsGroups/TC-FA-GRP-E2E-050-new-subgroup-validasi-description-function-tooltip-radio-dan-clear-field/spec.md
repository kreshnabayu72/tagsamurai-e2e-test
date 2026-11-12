---
id: TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field
title: "Popup New Subgroup: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field]"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-148
  - TC-FA-GRP-149
  - TC-FA-GRP-150
  - TC-FA-GRP-151
  - TC-FA-GRP-152
coverage:
  web: automated
---

# Popup New Subgroup: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field]

## Prerequisites

- Mode: FE+BE (backend nyata; hanya TC-FA-GRP-148 menyimpan subgroup dan membaca Detail, TC lain tanpa submit).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-050` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-149: Description 361 karakter. TC-FA-GRP-152: Name `Clear Sub {runId}-050`, Code `CLR2`, Description `Clear me`, Function Assignable, Stay tercentang (tidak disubmit). TC-FA-GRP-148: Name `Desc 360 Sub {runId}-050` dan Description 360 karakter.
- Kemampuan teknis: pengetikan 361 karakter; klik icon info Function (tooltip on click).
- Pemulihan (hook `before` dan `after`): hapus lewat API group dengan suffix `{runId}-050` dan group ber-Code literal `CLR2` yang dibuat spec ini.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-149: Description 361 karakter langsung error

1. Ketik Search `Head Office`, tekan Enter
2. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
3. Ketik Description 361 karakter
4. Verifikasi inline error `Max. 360 characters` langsung tampil

### TC-FA-GRP-150: Tooltip icon info Function (on click) per opsi

5. Klik icon info None
6. Verifikasi tooltip None: `This group is for organizing only. It won't hold assets.`
7. Klik icon info Assignable
8. Verifikasi tooltip Assignable: `Assets can be registered or transferred directly into this group.`

### TC-FA-GRP-151: Function radio mutually exclusive

9. Pilih Function Assignable
10. Pilih Function None
11. Verifikasi hanya satu opsi terpilih pada satu waktu (None terpilih)
12. Verifikasi Assignable otomatis tidak terpilih

### TC-FA-GRP-152: Tombol [Clear Field]

13. Isi Group Name `Clear Sub {runId}-050`, Code `CLR2`, Description `Clear me`, pilih Function Assignable, dan centang `Stay on this form after submitting`
14. Klik [Clear Field]
15. Verifikasi Group Name dikosongkan
16. Verifikasi Code dikosongkan
17. Verifikasi Description dikosongkan
18. Verifikasi Function kembali ke None
19. Verifikasi checkbox `Stay on this form after submitting` tidak ikut ter-reset (tetap tercentang)
20. Verifikasi tidak ada dialog konfirmasi
21. Hilangkan centang `Stay on this form after submitting`

### TC-FA-GRP-148: Description 360 karakter diterima

22. Isi Group Name `Desc 360 Sub {runId}-050` dan Description 360 karakter, lalu klik [Submit]
23. Verifikasi toast sukses `Success, group has been created.`
24. Klik Head Office di sidebar, ganti isi kotak Search dengan `Desc 360 Sub {runId}-050`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group
25. Verifikasi Description tersimpan utuh 360 karakter di Detail
26. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: kasus tanpa submit lebih dulu dalam satu pembukaan popup, lalu aksi sukses TC-FA-GRP-148 di akhir (S-10); berbeda dari urutan nomor TC sumber. Field dikosongkan oleh [Clear Field] sebelum TC-FA-GRP-148 (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 21 (Hilangkan centang `Stay on this form after submitting`); langkah 24 (Klik Head Office di sidebar, ganti isi kotak Search dengan `Desc 360 Sub {runId}-050`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group); langkah 26 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Pencarian baris target (S-03, R-16): langkah 1 (Ketik Search `Head Office`, tekan Enter) menemukan baris Head Office; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris Head Office tidak dijamin berada di halaman 1 All Groups.
- Temuan untuk QA:
  - TC-FA-GRP-148 Expected b "Description tersimpan utuh di Detail" tidak menyebut langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-152 menyebut "Isi/ubah seluruh field" tanpa data; spec memakai nilai bersuffix milik spec.

