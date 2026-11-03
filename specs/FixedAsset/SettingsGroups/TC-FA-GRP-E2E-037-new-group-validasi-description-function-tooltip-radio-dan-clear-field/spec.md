---
id: TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field
title: "Popup New Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan Tombol [Clear Field]"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-100
  - TC-FA-GRP-101
  - TC-FA-GRP-102
  - TC-FA-GRP-103
  - TC-FA-GRP-104
coverage:
  web: automated
---

# Popup New Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan Tombol [Clear Field]

## Prerequisites

- Mode: FE+BE (backend nyata; hanya TC-FA-GRP-100 menyimpan group dan membaca Detail, TC lain tanpa submit).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-037` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-101: Description 361 karakter. TC-FA-GRP-104: Name `Clear Test {runId}-037`, Code `CLR1`, Description `Clear me`, Function Assignable, Stay tercentang (tidak disubmit). TC-FA-GRP-100: Name `Desc 360 {runId}-037` dan Description 360 karakter.
- Kemampuan teknis: pengetikan 361 karakter; hover/klik icon info Function (tooltip on click).
- Pemulihan (hook `after`): hapus lewat API group dengan suffix `{runId}-037` yang dibuat TC-FA-GRP-100.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-101: Description 361 karakter langsung error

1. Klik [+] Group di sidebar
2. Ketik Description 361 karakter
3. Verifikasi inline error `Max. 360 characters` langsung tampil

### TC-FA-GRP-102: Tooltip icon info Function (on click) per opsi

4. Klik icon info None
5. Verifikasi tooltip None: `This group is for organizing only. It won't hold assets or appear as a disposal destination.`
6. Klik icon info Assignable
7. Verifikasi tooltip Assignable: `Assets can be registered or transferred directly into this group.`
8. Klik icon info Disposal Group
9. Verifikasi tooltip Disposal Group: `This group becomes a destination for disposed assets. You can have more than one Disposal Group.`

### TC-FA-GRP-103: Function radio mutually exclusive

10. Pilih Function Assignable
11. Pilih Function Disposal Group
12. Verifikasi hanya satu opsi terpilih pada satu waktu (Disposal Group terpilih)
13. Verifikasi Assignable otomatis tidak terpilih

### TC-FA-GRP-104: Tombol [Clear Field]

14. Isi Group Name `Clear Test {runId}-037`, Code `CLR1`, Description `Clear me`, pilih Function Assignable, dan centang `Stay on this form after submitting`
15. Klik [Clear Field]
16. Verifikasi Group Name dikosongkan
17. Verifikasi Code dikosongkan
18. Verifikasi Description dikosongkan
19. Verifikasi Function kembali ke None
20. Verifikasi checkbox `Stay on this form after submitting` tidak ikut ter-reset (tetap tercentang)
21. Verifikasi tidak ada dialog konfirmasi
22. Hilangkan centang `Stay on this form after submitting`

### TC-FA-GRP-100: Description 360 karakter diterima

23. Isi Group Name `Desc 360 {runId}-037` dan Description 360 karakter, lalu klik [Submit]
24. Verifikasi toast sukses `Success, group has been created.`
25. Ketik Search `Desc 360 {runId}-037`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group
26. Verifikasi Description tersimpan utuh 360 karakter di Detail
27. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: kasus tanpa submit lebih dulu dalam satu pembukaan popup (prinsip "halaman yang sama dipakai berulang"), lalu aksi sukses TC-FA-GRP-100 di akhir (S-10); berbeda dari urutan nomor TC sumber. Field dikosongkan oleh [Clear Field] sebelum TC-FA-GRP-100 (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 22 (Hilangkan centang `Stay on this form after submitting`); langkah 25 (Ketik Search `Desc 360 {runId}-037`, tekan Enter, lalu klik nama group...); langkah 27 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Temuan untuk QA:
  - TC-FA-GRP-100 Expected b "Description tersimpan utuh di Detail" tidak menyebut langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-104 menyebut "Isi/ubah seluruh field" tanpa data; spec memakai nilai bersuffix milik spec.

