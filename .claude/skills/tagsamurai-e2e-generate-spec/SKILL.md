---
name: tagsamurai-e2e-generate-spec
description: Workflow untuk menurunkan TC granular (tc-[modul].md) menjadi spec.md e2e TestSpectra untuk satu submodul TAG Samurai. Dipakai saat membuat suite baru atau menambah spec e2e dari TC granular.
---

# Generate Spec E2E dari TC Granular

Aturan lengkap ada di `docs/e2e-conventions.md`. Baca dokumen itu dulu, lalu ikuti alur ini. Skill framework `spec-and-suite-authoring` dan `workspace-structure` tetap berlaku.

## Input yang wajib ada

1. Path `tc-[modul].md` (TC granular) dan kalau ada `tc-[modul]-backend.md` (untuk mengenali TC hanya-BE).
2. Kode prefix modul dari `foundation/tc-prefix-registry.md` (contoh `GS` + `USER`).
3. Cakupan yang diminta (seluruh submodul, satu section, atau daftar TC).

Kalau salah satu tidak ada, berhenti dan tanyakan. Jangan menebak prefix.

## Langkah

1. **Baca TC sumber** sampai tabel Data Uji Pre-setup dan Data Uji Dinamis, bukan hanya baris TC-nya.
2. **Seleksi** dengan bagian 2 konvensi: semua TC masuk spec kecuali yang hanya-BE. Kasus hanya-FE (tampilan murni, tooltip, Setup Column, hover, keystroke, kegagalan server) tetap masuk sebagai spec dengan `Mode: mock` di `## Prerequisites`; kasus yang memukul backend nyata masuk sebagai spec FE+BE. Hambatan teknis dan label "Manual" bukan alasan mengeluarkan TC: tulis semua kebutuhan (data, akun, waktu, kuota, race, pemicu kegagalan, kemampuan teknis) di `## Prerequisites` sebagai sumber resmi bagi tim FE. `## Notes` hanya penjelasan tambahan. Buat daftar TC yang masuk dan yang hanya-BE.
3. **Kelompokkan** sesuai prinsip bagian 3 konvensi: satu spec = satu topik aksi yang bisa dijalankan berurutan, screening di awal, validasi yang diblokir sebelum aksi sukses, aksi yang menghapus data di akhir, kasus menutup form di akhir, variasi topik yang sama berurutan. Pisahkan topik aksi berbeda yang butuh kondisi data bervariasi (Delete, Toggle Active, Remove Access), beda entity, bergantung hardware, atau pembuat data yang perlu dipisah dari yang tidak. Kasus blokir karena kondisi data target (bukan validasi field dan bukan blokir identitas atau role) dijadikan spec sendiri per topik (prinsip 12). Beri tiap TC label kelas harness (prinsip 13: defense-in-depth, fault injection, multi-konteks, harness eksternal, volume data, binary buffer, absence log, state tenant) dan jangan taruh TC berkelas harness di spec screening atau fungsional biasa; satu spec = satu kelas. Kelas ringan (defense-in-depth tanpa harness eksternal, fault injection) cukup satu spec per kelas per modul, bukan per aksi; kelas berat (multi-konteks, harness eksternal, volume data) satu spec per jenis harness. Spec yang diperkirakan melewati sekitar 35 langkah atau memuat lebih dari satu kelas ditinjau ulang sebelum rencana diajukan. Kasus izin per role mengikuti bagian 3a (Role Matrix): spec positif dan negatif per aksi, satu spec untuk banyak role. Catat data mana yang harus dibuat sendiri per spec (bagian 5) dan berapa kali form dibuka.
4. **Tampilkan rencana ke user dan tunggu persetujuan** sebelum menulis file. Rencana berisi tabel:
   `spec (id + judul)` | `sourceTc` | `role/precondition` | `data` | `hook/step yang dibutuhkan` | `kelas harness` | `jumlah langkah (perkiraan)` | `mode (FE+BE / mock)` | `TC hanya-BE`.
5. Setelah disetujui, buat di `specs/<ModulBesar>/<SubModul>/` (PascalCase, contoh `specs/GlobalSettings/User/`):
   - `suite.md` hanya jika belum ada (`id: suite-<kebab>`, `parallel: true` hanya jika semua spec independen). Kalau sudah ada, pakai apa adanya.
   - `TC-<ModulBesar>-<SubModul>-E2E-<NNN>-<slug>/spec.md`, dengan `NNN` melanjutkan nomor terakhir di suite itu.
6. Isi frontmatter sesuai bagian 8 konvensi, termasuk `sourceTc` (daftar id TC granular) dan `status: draft`. `caseType` spec gabungan ikut jenis alur utama yang dominan (bagian 8 konvensi). `coverage.web: automated` untuk spec yang dirancang untuk otomasi, progres dibaca dari `status`.
7. Tulis body spec.md:
   - Tulis dalam bahasa Indonesia (bagian 7 konvensi). Teks yang tampil di aplikasi (tombol, toast, tooltip, pesan error, judul dialog) ditulis persis seperti di aplikasi. Slug pada `id` tetap bahasa Inggris.
   - `# <title>` sama dengan `title`.
   - `## Prerequisites`: role, data pre-setup, dan hook yang dipakai. Untuk spec Role Matrix, tabel "Role yang diuji".
   - `## Test Steps`: langkah bernomor, konkret, satu aksi per baris. Jangan menulis `@step:<nama>` di tahap ini: `spectra lint` mewajibkan setiap `@step` punya panggilan `Step.<nama>()` di script, sehingga spec tanpa script akan gagal lint. Tulis langkah berulang sebagai teks biasa. `@step` ditambahkan oleh skill `tagsamurai-e2e-generate-script` saat Step-nya dibuat.
   - Label tombol dan cara menutup form mengikuti bagian 9 konvensi (`[Submit]` untuk Create, `[Save]` untuk Edit, `[Clear Field]`, `✕`/`Esc`, tidak ada `[Cancel]` pada modal). Cek ke `prd-conventions.md` §24.1, jangan menyalin dari TC karena TC bisa salah.
   - Spec panjang diberi subjudul `###` di dalam `## Test Steps`.
   - Nilai data mengacu ke fixture (`Fixture.<berkas>.<kunci>`), bukan ditulis mentah.
   - Expected result ditulis sebagai langkah `Verifikasi ...` yang bisa langsung menjadi assertion.
8. Jalankan `spectra lint --strict specs/<Suite>` dan perbaiki sampai bersih.
9. Update `docs/coverage/<Suite>.md`: pemetaan TC granular ke spec, alasan TC hanya-BE, dan tabel "Lapisan per TC" (Spec, Mode).
10. Laporkan ke user: daftar spec, TC yang dilewati, dan hal yang butuh keputusan. Jangan lanjut membuat `web.test.ts`, itu skill `tagsamurai-e2e-generate-script`.

## Larangan

- Jangan mengubah isi atau nomor TC granular. Kalau menemukan masalah di TC sumber, catat sebagai temuan untuk QA.
- Jangan merenumber id spec yang sudah ada.
- Jangan mengubah `ARCHITECTURE.md`, `spectra.config.ts`, `package.json`, atau spec suite lain tanpa izin.
- Jangan menyimpan password atau token di spec dan fixture.
- Jangan membuat spec yang bergantung pada hasil spec lain.
