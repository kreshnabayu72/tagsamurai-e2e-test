---
id: TC-FA-GRP-E2E-051-new-subgroup-hover-saving-submit-double-click-dan-aksesibilitas
title: "Popup New Subgroup: Hover dan Saving State [Submit], Double-Click, dan Aksesibilitas"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-153
  - TC-FA-GRP-157
  - TC-FA-GRP-159
coverage:
  web: automated
---

# Popup New Subgroup: Hover dan Saving State [Submit], Double-Click, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-153 dan TC-FA-GRP-159 menyimpan subgroup; respons simpan ditahan lewat intercept hanya untuk mengamati state saving, bukan kegagalan yang dipaksa).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-051` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-153: Name `Hover Save Sub {runId}-051`. TC-FA-GRP-159: Name `Double Click Sub {runId}-051`.
- Kebutuhan intercept (`Spectra.intercept()`): menahan respons simpan group pada langkah 13 dan melepasnya pada langkah 16; nama endpoint tidak disebut di TC dan PRD (ditentukan tim FE di tahap script). Intercept dilepas di hook `after` bila spec gagal di tengah.
- Kemampuan teknis: pembacaan atribut ARIA (`aria-required`, `aria-describedby`) dan fokus keyboard (Tab berulang); double-click cepat; pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD).
- Pemulihan (hook `after`): lepas intercept; hapus lewat API group dengan suffix `{runId}-051`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-157: Aksesibilitas Popup New Subgroup

1. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
2. Klik [Submit] dengan form kosong
3. Verifikasi Group Name ber-`aria-required`
4. Verifikasi error terhubung ke Group Name via `aria-describedby`
5. Tekan Tab berulang
6. Verifikasi fokus berputar di dalam popup (focus trap)
7. Tekan Esc
8. Verifikasi Esc menutup popup

### TC-FA-GRP-153: Hover dan Saving state tombol [Submit]

9. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
10. Isi Group Name `Hover Save Sub {runId}-051`
11. Hover [Submit]
12. Verifikasi [Submit] menampilkan state hover
13. Tahan respons simpan group lewat intercept
14. Klik [Submit]
15. Verifikasi [Submit] masuk saving state (disabled + loading)
16. Lepas tahanan respons dan tunggu popup tertutup

### TC-FA-GRP-159: Double-click [Submit] hanya 1 request

17. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
18. Isi Group Name `Double Click Sub {runId}-051`
19. Tunggu toast lama hilang otomatis
20. Catat jumlah group lewat fixture BE sebagai baseline TC-FA-GRP-159
21. Double-click cepat [Submit]
22. Verifikasi tombol [Submit] disabled setelah klik pertama
23. Verifikasi hanya 1 toast sukses `Success, group has been created.`
24. Verifikasi hanya 1 record dibuat: jumlah group lewat fixture BE = baseline TC-FA-GRP-159 + 1

## Notes

- Mode: FE+BE (backend nyata, intercept hanya menahan respons untuk mengamati saving state; bukan kegagalan yang dipaksa sehingga bukan kelas b). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-157 (submit kosong, diblokir) lebih dulu, lalu TC-FA-GRP-153 dan TC-FA-GRP-159 yang menyimpan subgroup (S-10); berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 13 (Tahan respons simpan group lewat intercept); langkah 16 (Lepas tahanan respons dan tunggu popup tertutup); langkah 19 (Tunggu toast lama hilang otomatis); langkah 20 (Catat jumlah group lewat fixture BE sebagai baseline TC-FA-GRP-159).
- Temuan untuk QA:
  - TC-FA-GRP-159 Expected b "Tombol disabled setelah klik pertama" adalah state sementara; diasersi tepat setelah double-click (8b butir 5). Jika popup sudah menutup sebelum asersi, tim script perlu menahan respons seperti langkah 13; TC tidak menyebut penundaan respons.
  - TC-FA-GRP-157 Expected c "dialog Unsaved changes bila ada perubahan" bersyarat dan tidak punya langkah perubahan di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-153 Expected b "sampai response" tidak menyebut keadaan setelah respons; spec hanya menunggu popup tertutup (langkah 16) tanpa `Verifikasi` tambahan.

